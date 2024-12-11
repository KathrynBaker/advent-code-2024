import pandas as pd

disk_map = "12345"
# disk_map = "2333133121414131402"
#
# with open("inputs/dec9_input.txt", "r") as file:
#     disk_map = file.read()
#
def check_even(number):
    if number & 1:
        return False
    return True

# def build_reversed_array(list, val):
#     return [value for value in list if value != val]
#
# # diskmap to index and space
# file_index = 1
# disk_content = []
# for i in range(len(disk_map)):
#     #print(disk_map[i])
#     if i == 0:
#         add_value = "0"
#     elif not check_even(i):
#         add_value = "."
#     else:
#         add_value = str(file_index)
#         file_index += 1
#     for j in range(int(disk_map[i])):
#         disk_content.append(add_value)
#
# print(disk_content)
#
# # reorder the disk map
# reversed_content = disk_content.copy()
#
# reversed_content = build_reversed_array(disk_content, ".")
# reversed_content.reverse()
# start_len_reversed = len(reversed_content)
# print(reversed_content)
# for i in range(len(disk_content)):
#     # print(disk_content[i])
#     if disk_content[i] == ".":
#         #print("It's a .")
#         looking_for_num = True
#         while looking_for_num:
#             #print(reversed_content[0])
#             if reversed_content[0] == ".":
#                 del reversed_content[0]
#             else:
#                 disk_content[i] = reversed_content[0]
#                 del reversed_content[0]
#                 looking_for_num = False
#
# print(reversed_content)
# print(disk_content)
#
# print(start_len_reversed)
# print(len(reversed_content))
#
# for i in range(start_len_reversed - len(reversed_content)):
#     disk_content[i + start_len_reversed] = "."
#
# print(disk_content)
#
# running_total = 0
# for i in range(len(disk_content)):
#     if disk_content[i] != ".":
#         running_total += i * int(disk_content[i])
#
# print(running_total)

disk_map = "12345"
disk_map = "2333133121414131402"
disk_lookup = []
disk_sizes = {}
# diskmap to index and space
file_index = 1
disk_content = []
for i in range(len(disk_map)):
    #print(disk_map[i])
    #print(disk_lookup)
    if i == 0:
        add_value = "0"
        disk_lookup.append(["0", disk_map[i], disk_map[i + 1]])
        disk_sizes["0"] = {"type": "file", "size": disk_map[i], "location": i}
    elif not check_even(i):
        add_value = "."
        disk_sizes[str(file_index) + "s"] = {"type": "space", "size": disk_map[i], "location": i}
    else:
        add_value = str(file_index)
        try:
            disk_lookup.append([file_index, disk_map[i], disk_map[i + 1]])
        except IndexError:
            disk_lookup.append([file_index, disk_map[i], "0"])
        disk_sizes[file_index] = {"type": "file", "size": disk_map[i], "location": i}
        file_index += 1
    for j in range(int(disk_map[i])):
        disk_content.append(add_value)

print(disk_content)
#print(disk_lookup)
print(disk_sizes)

#get last file size which is <= to value

reversed_keys = reversed(disk_sizes.keys())
# reset file index to last value
file_index += -1
print(file_index)
print(disk_sizes[file_index - 1])
new_layout = {}
current_location = 0
# need to do files over spaces, so it's start with the highest indexed file, and move it to the first available space, so not the qay round I'm currently doing!
for entry in disk_sizes.keys():
    print("start loop")
    # print(disk_sizes[entry])
    if disk_sizes[entry]["type"] == "space":
        print("Having a look")
        for i in range(file_index, current_location, -1):
            # print(i)
            print(disk_sizes[i])
            if disk_sizes[i]["type"] == "file":
                if disk_sizes[i]["size"] <= disk_sizes[entry]["size"]:
                    print("I can move this one here")
    else:
        new_layout[entry] = disk_sizes[entry]
    current_location += 1

print(new_layout)


