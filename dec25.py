import os
from collections import Counter
import pandas as pd


day = 25
use_example = False


def get_file_path(day_to_use, example):
    if example:
        return os.path.join("example_inputs", "dec" + str(day_to_use) + "_input_example.txt")
    else:
        return os.path.join("inputs", "dec" + str(day_to_use) + "_input.txt")


with open(get_file_path(day, use_example), "r") as file:
    file_content = file.read()

lines = file_content.split("\n")

frames = {}
frames_index = 0
frame = []
for line in lines:
    try:
        line_type = line[0]
        frame.append(list(line))
    except IndexError:
        frames[frames_index] = frame
        frames_index += 1
        frame = []

virtual_keys = []
virtual_locks = []
for thing in frames.keys():
    df = pd.DataFrame(frames[thing])
    pattern = []
    for name in df.columns:
        pattern.append(int(df[name].value_counts().get("#", 0))-1)
    if (frames[thing][0][0]) == "#":
        is_lock = True
        virtual_locks.append(pattern)
    else:
        is_lock = False
        virtual_keys.append(pattern)

# print("The locks are:")
# for entry in virtual_locks:
#     print(entry)
# print("The keys are:")
# for entry in virtual_keys:
#     print(entry)

valid_count = 0
for virtual_lock in virtual_locks:
    for virtual_key in virtual_keys:
        is_valid = True
        for x in range(len(virtual_key)):
            if virtual_key[x] + virtual_lock[x] > 5:
                is_valid = False
        if is_valid:
            valid_count += 1

print(f"The number of locks that fit are {valid_count}")