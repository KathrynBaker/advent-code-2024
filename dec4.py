import pandas as pd
import numpy as np
import re
from collections import Counter

test_pattern = "XMAS"
file_name = 'example_inputs/dec4_input_example.txt'

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

print("Found in rows = " + str(number_found))

# check the columns
for i in range(number_of_cols-1):
    number_found = number_found + number_of_pattern_found(test_pattern, df[i])

print("Found in rows and columns = " + str(number_found))

a = df.to_numpy()

diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))

for entry in diags:
    number_found = number_found + number_of_pattern_found(test_pattern, entry)


print("Found in all = " + str(number_found))

print(df)
for i in range(number_of_cols-1):
    x = df[i]
    print(x)
    for j in range(len(x)):
        print(df[i][j])

    #number_found = number_found + number_of_pattern_found(test_pattern, df[i])

