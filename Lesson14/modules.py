from enum import Enum
import math as mat
import random as rand

for items in dir(rand):
    print(items)

for items in dir(mat):
    print(items)

# Import custom module
import custom_module
print(custom_module.randomfunfact())
print(custom_module.bird)

# Don't understand
print(__name__)
print(custom_module.__name__)

# import rock_paper_scissors
from rps7 import rock_paper_scissors

rock_paper_scissors()

