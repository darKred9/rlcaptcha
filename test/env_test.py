import os
import sys

# get this file's dir as TEST_DIR
TEST_DIR = os.path.abspath(os.path.dirname(__file__))
# get the parent dir of TEST_DIR (the ROOT dir of the project)
sys.path.insert(0, os.path.dirname(TEST_DIR))

from RL.env import env

text = env(10,10,10, 1.0)
print(text)

