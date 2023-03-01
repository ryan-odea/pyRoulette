import random
from sys import platform
import penalty

chambers = 6

if random.randint(1, chambers) == 1:
    if platform == "Darwin":
        penalty.darwin_enforcer()
    if platform == "Windows":
        penalty.win_enforcer()
else:
    print("Safe!")
