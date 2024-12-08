import pandas as pd
import numpy as np
import re
from collections import Counter

test_pattern = "XMAS"
file_name = 'example_inputs/dec4_input_example.txt'
file_name = 'inputs/dec4_input.txt'

def number_of_pattern_found(pattern, char_list):
    forward_test = "".join(char_list)
    reverse_test = forward_test[::-1]
    found_forward = re.findall(pattern, forward_test)
    found_reversed = re.findall(pattern, reverse_test)
    found = found_reversed + found_forward
    return len(found)


# Build the column delimiters as single characters using length of the first row
with open(file_name) as f:
    first_line = f.readline()

number_of_cols = len(first_line)
colspecs = []
for i in range(number_of_cols-1):
    colspecs.append((i, i+1))

# Get the data frame
df = pd.read_fwf(file_name, header=None, colspecs=colspecs)

number_found = 0
# Check the rows
for i in range(len(df)):
    number_found = number_found + number_of_pattern_found(test_pattern, df.iloc[i].tolist())

# print("Found in rows = " + str(number_found))

# check the columns
for i in range(number_of_cols-1):
    number_found = number_found + number_of_pattern_found(test_pattern, df[i])

# print("Found in rows and columns = " + str(number_found))

a = df.to_numpy()

diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))

for entry in diags:
    number_found = number_found + number_of_pattern_found(test_pattern, entry)


# print("Found in all = " + str(number_found))

print(df)
# for i in range(number_of_cols-1):
#     x = df[i]
#     print(x)
#     for j in range(len(x)):
#         print(df[i][j])

    #number_found = number_found + number_of_pattern_found(test_pattern, df[i])


# print(len(df))
# print(df.shape[0])
shape = df.shape
total = 0
for row_step in range(shape[0] - 2):
    for col_step in range(shape[1] - 2):
        col_index = col_step + 1
        row_index = row_step + 1
        if df[col_index][row_index] == "A":
            # print("It's the A")
            # check for the M or S top left of the A
            if ((df[col_index - 1][row_index - 1] == "M" and df[col_index + 1][row_index + 1] == "S") or \
                    (df[col_index - 1][row_index - 1] == "S" and df[col_index + 1][row_index + 1] == "M")) and \
                    ((df[col_index + 1][row_index - 1] == "M" and df[col_index - 1][row_index + 1] == "S") or \
                     (df[col_index + 1][row_index - 1] == "S" and df[col_index - 1][row_index + 1] == "M")):
                # print("This is good")
                total += 1

print(total)

