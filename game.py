import random
import penalty

chambers = 6

if random.randint(1, chambers) == 1:
    penalty.enforcer()
else:
    print("Safe!")
