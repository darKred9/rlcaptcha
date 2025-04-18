import os
import numpy as np
import torch
import gym
from gym import spaces
from stable_baselines3 import PPO
from stable_baselines3.common.utils import set_random_seed

from utils.path_utils import get_path_from_project_root
from RL.env import env
# from RL.example_solver import example_solver_pil
from RL.real_ai_solver import solve
from RL.reward import reward_func

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

if not torch.cuda.is_available():
    assert False, "GPU is not abvailable!"

os.makedirs(get_path_from_project_root("results"), exist_ok=True)

ACTION_BOUNDS = {
    'noise_dots_number': (0, 100),
    'noise_dots_thickness': (1, 30),
    'rotation_angle': (0, 60),
    'char_spacing': (0.0, 1.0)
}

class CaptchaEnv(gym.Env):
    def __init__(self):
        super(CaptchaEnv, self).__init__()
        self.action_space = spaces.Box(low=-1, high=1, shape=(4,), dtype=np.float32)
        self.observation_space = spaces.Box(low=0, high=1, shape=(4,), dtype=np.float32)
        
        self.state = np.zeros(4, dtype=np.float32)
        self.reward_history = []
        self.best_params = None
        self.best_reward = -1
        self.step_count = 0

    def step(self, action):
        """
        1. the action is known
        2. step() is called to move a step and get the reward of this step
        """

        # denormalized the action back to the real range
        noise_dots_number = int(self._denormalize(action[0], *ACTION_BOUNDS['noise_dots_number']))
        noise_dots_thickness = int(self._denormalize(action[1], *ACTION_BOUNDS['noise_dots_thickness']))
        rotation_angle = self._denormalize(action[2], *ACTION_BOUNDS['rotation_angle'])
        char_spacing = self._denormalize(action[3], *ACTION_BOUNDS['char_spacing'])
        
        # generate a captcha based on the action
        text_answer = env(noise_dots_number, noise_dots_thickness, rotation_angle, char_spacing)
        
        # get the guess by the AI solver
        captcha_path = get_path_from_project_root("results", "captcha1.png")
        text_recog = solve(captcha_path) # solve by the real AI solver
        
        # calculate the reward
        reward = reward_func(text_answer, text_recog)
        self.reward_history.append(reward)
        
        # set states
        rewards_window = self.reward_history[-4:] + [0] * (4 - min(4, len(self.reward_history)))
        self.state = np.array(rewards_window[:4], dtype=np.float32)
        
        # update the best reward
        recent_reward = np.mean(self.reward_history[-10:]) if len(self.reward_history) >= 10 else np.mean(self.reward_history)
        if recent_reward > self.best_reward and reward > 0:
            self.best_reward = recent_reward
            self.best_params = {
                'noise_dots_number': noise_dots_number,
                'noise_dots_thickness': noise_dots_thickness, 
                'rotation_angle': rotation_angle,
                'char_spacing': char_spacing
            }
        
        info = {
            'parameters': {
                'noise_dots_number': noise_dots_number,
                'noise_dots_thickness': noise_dots_thickness,
                'rotation_angle': rotation_angle,
                'char_spacing': char_spacing
            },
            'text_answer': text_answer,
            'text_recognized': text_recog,
            'reward': reward
        }
        
        # do print every 20 steps
        self.step_count += 1
        if self.step_count % 20 == 0:
            print(f"steps: {self.step_count}")
            
            print(f"inputs (action): \
                  noise_dots_number: {noise_dots_number}, \
                  noise_dots_thickness:{noise_dots_thickness}, \
                  rotation_angle: {rotation_angle:.2f}, \
                  char_spacing: {char_spacing:.2f}")
            
            print(f"Correct Answer: {text_answer}; \
                  Guess from the AI solver: {text_recog}, \
                  reward: {reward}")
            
            if self.best_params:
                print(f"Best Inputs: {self.best_params}")
                print(f"Best Reward: {self.best_reward:.2f}")
            
            print("-" * 40)
        
        done = False # termination is controlled by the fixed training steps instead of the reward.

        return self.state, reward, done, info

    def reset(self):
        if len(self.reward_history) > 1000: 
            self.reward_history = self.reward_history[-1000:]
            
        rewards_window = self.reward_history[-4:] + [0] * (4 - min(4, len(self.reward_history)))
        self.state = np.array(rewards_window[:4], dtype=np.float32)
        return self.state

    def _denormalize(self, normalized_value, min_val, max_val):
        return min_val + (normalized_value + 1) * 0.5 * (max_val - min_val)

def train():

    env = CaptchaEnv()
    
    set_random_seed(42)
    
    LOG_PATH = get_path_from_project_root("tensorboard_logs")

    model = PPO(
        "MlpPolicy", 
        env,
        verbose=1,
        device=device,
        learning_rate=3e-4,
        batch_size=64,
        ent_coef=0.01,
        clip_range=0.2,
        tensorboard_log=LOG_PATH
    )
    
    print("start training:")
    model.learn(total_timesteps=1000)
    
    PPO_MODEL_PATH = get_path_from_project_root("model", "ppo_captcha_model")
    model.save(PPO_MODEL_PATH)
    
    if env.best_params:
        print("\nbest inputs:")
        print(env.best_params)
        print(f"best reward：{env.best_reward:.2f}")
    else:
        assert False, "No best_params!"
    
    return env.best_params


if __name__ == "__main__":
    train()
