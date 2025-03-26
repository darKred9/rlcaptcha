import os
import sys

# get this file's dir as TEST_DIR
TEST_DIR = os.path.abspath(os.path.dirname(__file__))
# get the parent dir of TEST_DIR (the ROOT dir of the project)
sys.path.insert(0, os.path.dirname(TEST_DIR))

from utils.path_utils import get_path_from_project_root

from RL.env import env
from RL.example_solver import example_solver_pil

text = env(10,10,10,1.0)
print(text)

captcha_path = get_path_from_project_root("results", "captcha1.png")
text = example_solver_pil(captcha_path)
print(f"Recognization result: {text}")



