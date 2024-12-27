import os

day = 22
use_example = False


def get_file_path(day_to_use, example):
    if example:
        return os.path.join("example_inputs", "dec" + str(day_to_use) + "_input_example.txt")
    else:
        return os.path.join("inputs", "dec" + str(day_to_use) + "_input.txt")


with open(get_file_path(day, use_example), "r") as file:
    file_content = file.read()

modulo_value = 16777216
init_number = 123


def to_next_number(current_number):
    # Step 1 has the multiply by 64
    current_number = (current_number ^ (current_number * 64)) % modulo_value
    # Step 2 has a divide by 32
    current_number = (current_number ^ (current_number // 32)) % modulo_value
    # Step 3 has a multiply by 2048
    current_number = (current_number ^ (current_number * 2048)) % modulo_value
    return current_number


buyers_starts = [1, 10, 100, 2024]
buyers_starts = file_content.split("\n")
buyers_starts = [int(item) for item in buyers_starts]
total = 0
for secret in buyers_starts:
    for i in range(2000):
        secret = to_next_number(secret)
    total += secret

print(total)

