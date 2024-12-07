# https://adventofcode.com/2024/day/2

import pandas as pd
from collections import Counter


def safe_or_unsafe(record):
    direction = "TBC"
    for j in range(len(consider)-1):
        if consider[j] == consider[j + 1]:
            return "UNSAFE"
        if abs(consider[j] - consider[j + 1]) > 3:
            return "UNSAFE"
        if consider[j] < consider[j+1]:
            match direction:
                case "TBC":
                    direction = "ASC"
                case "DESC":
                    return "UNSAFE"
                case "ASC":
                    if j == len(consider)-2:
                        return "SAFE"
        if consider[j] > consider[j+1]:
            match direction:
                case "TBC":
                    direction = "DESC"
                case "ASC":
                    return "UNSAFE"
                case "DESC":
                    if j == len(consider)-2:
                        return "SAFE"


df = pd.read_table("inputs/dec2_input.txt", header=None, sep=" ", names=range(9))
safe_unsafe = []
check = []
for i in range(len(df)):
    test = df.iloc[i].tolist()
    print(test)
    consider = []
    for entry in test:
        if pd.notna(entry):
            consider.append(entry)
    print(consider)
    record_result = safe_or_unsafe(consider)
    if record_result == "UNSAFE":
        check.append(consider)
    safe_unsafe.append(record_result)


safe_or_unsafe_numbers = Counter(safe_unsafe)
print(safe_unsafe)
print(safe_or_unsafe_numbers["SAFE"])
print(safe_or_unsafe_numbers["UNSAFE"])
print(len(check))

made_safe = 0
for entry in check:
    print(entry)
    for i in range(len(entry)):
        consider = entry.copy()
        del consider[i]
        print(consider)
        record_result = safe_or_unsafe(consider)
        if record_result == "SAFE":
            made_safe += 1
            break

print(safe_or_unsafe_numbers["SAFE"] + made_safe)
