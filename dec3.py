import re

pattern = "mul\([0-9]+,[0-9]+\)"
pat = re.compile(pattern)

with open("inputs/dec3_input.txt", "r") as file:
    file_content = file.read()

print(re.search(pattern, file_content))
print(len(file_content))
# test = re.findall(pattern, file_content)
test = []
offset = 0
loop = True
append = True
interact = file_content
iter = 0
while loop:
    print(interact)
    first_do = re.search(r"do\(\)", interact)
    first_dont = re.search(r"don't\(\)", interact)
    first_mul = re.search(pattern, interact)
    starts = []
    try:
        first_do_start = first_do.span()[0]
        first_do_stop = first_do.span()[1]
        starts.append(first_do_start)
    except AttributeError:
        first_do_start = len(file_content)
        starts.append(len(file_content))
    try:
        first_dont_start = first_dont.span()[0]
        first_dont_stop = first_dont.span()[1]
        starts.append(first_dont_start)
    except AttributeError:
        first_dont_start = len(file_content)
        starts.append(len(file_content))
    try:
        first_mul_start = first_mul.span()[0]
        first_mul_stop = first_mul.span()[1]
        starts.append(first_mul_start)
    except AttributeError:
        first_mul_start = len(file_content)
        starts.append(len(file_content))
    if min(starts) == first_mul_start:
        if append:
            test.append(interact[first_mul_start:first_mul_stop])
        interact = interact[first_mul_stop:]
        print(interact)
    if min(starts) == first_dont_start:
        append = False
        interact = interact[first_dont_stop:]
    if min(starts) == first_do_start:
        append = True
        interact = interact[first_do_stop:]
    if len(interact) < 6:
        loop = False
    iter += 1

print(test)


total = 0
for thing in test:
    res = tuple(map(int, thing[4:-1].split(',')))
    total += res[0]*res[1]

print(total)

