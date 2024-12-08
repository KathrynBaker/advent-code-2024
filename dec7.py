# https://adventofcode.com/2024/day/7
import os

# Settings
day = 7
use_example = False


def get_file_path(day_to_use, example):
    if example:
        return os.path.join("example_inputs", "dec" + str(day_to_use) + "_input_example.txt")
    else:
        return os.path.join("inputs", "dec" + str(day_to_use) + "_input.txt")


def get_aim_and_values(line_to_split):
    interim_aim = int(line.split(":")[0])
    interim_values = line.split(" ")
    interim_values.remove(interim_values[0])
    return interim_aim, [int(value) for value in interim_values]


def add_two_values(value1, value2):
    return value1 + value2


def multiply_two_values(value1, value2):
    return value1 * value2


with open(get_file_path(day, use_example), "r") as file:
    file_content = file.read()


available_operators = ["+", "*"]

line = "190: 10 19"
line = "3267: 81 40 27"
total = 0
rows = file_content.split("\n")

for line in rows:
    (aim, values) = get_aim_and_values(line)
    print(aim)
    print(values)
    new_running_values = [values[0]]
    number_of_operands = len(values)-1
    for i in range(number_of_operands):
        running_values = new_running_values.copy()
        new_running_values = [0]
        for running_value in running_values:
            try_add = add_two_values(running_value, values[i + 1])
            # print(try_add)
            try_mult = multiply_two_values(running_value, values[i + 1])
            # print(try_mult)
            # print("----")
            # print(i+1 == number_of_operands)
            # print(i+1)
            # print(number_of_operands)
            # print("----")
            if i+1 == number_of_operands:
                if (try_add == aim) or (try_mult == aim):
                    total += aim
                    print("Aim reached")
                    break
                else:
                    print("Not valid")
                    break
            if try_add > aim or try_mult > aim:
                print("Not an option")
            if try_add < aim:
                new_running_values.append(try_add)
            if try_mult < aim:
                new_running_values.append(try_mult)

print(total)
