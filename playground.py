# get the /data/train_val_list.txt's row number

import os
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))

# get the /data/train_val_list.txt's each row in a list element
with open(current_dir + '/data/train_val_list.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

# print the first 10 lines and last 10 lines

print('first 10 lines: ', lines[:10])
print('last 10 lines: ', lines[-10:])

