# https://adventofcode.com/2024/day/11

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import functools
import datetime
import pandas as pd

# Settings
day = 11
data = "125 17"  # example
data = "3935565 31753 437818 7697 5 38 0 123"  # full input
# ata = "0 12 3"

def check_even(number):
    if number & 1:
        return False
    return True


stones_array = []
# stones_array = data.split(" ")
for x in data.split(" "):
    stones_array.append(int(x))

# print(stones_array)


# @functools.cache
def update_stones_array(array_of_stones):
    # stones_list = [x for x in array_of_stones]
    # print(stones_list)
    # print("Updating List")
    # print(array_of_stones)
    # array_of_stones.loc[array_of_stones[0] == "0"] = 1
    # print(array_of_stones)
    new_stones_array = []
    # for x in array_of_stones.columns:
    for x in array_of_stones:
        # print("Hi")
        # print(array_of_stones[x][0])
        # test = array_of_stones[x][0]
        # print(test)
        # print(type(test))
        if array_of_stones[x][0] == 0:
            # print("0 to 1")
            new_stones_array.append("1")
            # array_of_stones.replace(to_replace=0, value=1, inplace=True)
            array_of_stones[x][0] = 1
        elif check_even(len(str(array_of_stones[x][0]))):
            # print("Even")
            str_entry = str(array_of_stones[x][0])
            split_point = int(len(str_entry)/2)
            left = int(str(array_of_stones[x][0])[:split_point])
            right = int(str(array_of_stones[x][0])[split_point:])
            # print(left)
            # print(right)
            array_of_stones[x][0] = left
            array_of_stones.insert(x+1, x, right, True)
            new_stones_array.append(str(left))
            new_stones_array.append(str(right))
        else:
            # print("Default")
            array_of_stones[x][0] = array_of_stones[x][0] * 2024
            new_stones_array.append(array_of_stones[x][0] * 2024)
        # print("Update is returning")
        # print(array_of_stones)
    array_of_stones.columns = [val for val in range(len(array_of_stones.columns))]
    # print(array_of_stones)
    new_frame = array_of_stones.copy()
    return new_stones_array


before = datetime.datetime.now()
# mapped_stones = map(str, stones_array)
# stones_array = mapped_stones

mapped_stones = pd.DataFrame([stones_array])
print(mapped_stones)
print(len(mapped_stones.columns))

for blink in range(25):
    stones_array = update_stones_array(stones_array)
    # print(new_stones_array)

verify = 0
# for x in mapped_stones:
#     print(x)
#     verify += 1
# print(stones_array)
print("-------------")
print(mapped_stones)
print(len(list(mapped_stones)))
print(verify)
print(datetime.datetime.now() - before)
