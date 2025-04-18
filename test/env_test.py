from utils.path_utils import get_path_from_project_root

from RL.env import env
from RL.example_solver import example_solver_pil
from RL.reward import reward_func
from RL.real_ai_solver import solve


import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

text_answer = env(64,15,51,0.83)
print(f"Answer: >{text_answer}<")

captcha_path = get_path_from_project_root("results", "captcha1.png")
text_recog = solve(captcha_path)
print(f"Recognization result: >{text_recog}<")

reward = reward_func(text_answer, text_recog)
print(f"Reward: >{reward}<")

