# https://adventofcode.com/2024/day/7
import os

# Settings
day = 7
use_example = True


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

total = 0
rows = file_content.split("\n")

rows = ["3267: 81 40 27"]

for line in rows:
    (aim, values) = get_aim_and_values(line)
    print(aim)
    print(values)
    new_running_values = [values[0]]
    number_of_operands = len(values)-1
    print(number_of_operands)
    for i in range(number_of_operands):
        running_values = new_running_values.copy()
        new_running_values = [0]
        testing = True
        prev_add_value = [values[0]]
        prev_mult_value = values[0]
        test_values = [values[0]]
        while testing:
            print(test_values)
            print("The for loop")
            limiter = len(test_values)-1
            print(len(test_values))
            for j in range(len(test_values) - 1):
                print(len(test_values))
                thing = test_values[j]
                print(thing)
                try_add = add_two_values(thing, values[i + 1])
                try_mult = multiply_two_values(thing, values[i + 1])
                test_values.remove(thing)
                print(test_values)
                if try_add <= aim:
                    test_values.append(try_add)
                if try_mult <= aim:
                    test_values.append(try_mult)
            print("Between for and if")
            print(test_values)
            if i + 1 == number_of_operands:
                print("End of run")
                print(test_values)
                testing = False
                if aim in test_values:
                    total += aim
                    print("Aim reached")
                    break
                else:
                    print("Not valid")
                    break



print(total)
