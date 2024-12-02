# https://adventofcode.com/2024/day/1
# Need to not overthink this
import pandas as pd
from collections import Counter


def get_distance(first_list, second_list):
    first_list.sort()
    second_list.sort()

    distance = 0
    for i in range(len(first_list)):
        distance += abs(first_list[i] - second_list[i])

    return distance


def get_similarity(first_list, second_list):
    counts_of_second = Counter(second_list)
    similarity = 0
    for entry in first_list:
        similarity += entry * counts_of_second[entry]
    return similarity


# df = pd.read_table("dec1_input.txt", header=None, names=["list1", "list2"], sep="   ")
# print(get_distance(df["list1"].tolist(), df["list2"].tolist()))

df = pd.read_table("dec1_input.txt", header=None, names=["list1", "list2"], sep="   ")
print(get_similarity(df["list1"].tolist(), df["list2"].tolist()))
