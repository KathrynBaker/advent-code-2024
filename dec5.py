# https://adventofcode.com/2024/day/5
import re
import pandas as pd
import io
import time
import random

class Rule:
    def __init__(self, value):
        self.value = value
        self.before = []
        self.after = []

    def __str__(self):
        response = "Rules for " + self.value + " must come before "
        response.join(self.before)
        response = response + " and after "
        response.join(self.after)
        return response

    def add_after(self, value):
        if value not in self.after:
            self.after.append(value)

    def add_before(self, value):
        if value not in self.before:
            self.before.append(value)


def rule_passing(_value, _line, _rules):
    _rules_kept = True
    _s1 = set(_line)
    if _value in _rules.keys():
        if _rules[_value].after:
            _s2 = set(_rules[_value].after)
            if _s1.intersection(_s2):
                _rules_kept = False
        if _rules[_value].before:
            _s2 = set(_rules[_value].after)
            if _s1.intersection(_s2):
                _rules_kept = False
    return _rules_kept


with open("dec5_input.txt", "r") as file:
    file_content = file.read()

rule_matches = re.findall(r"[0-9][0-9]\|[0-9][0-9]", file_content)
rules = {}
for entry in rule_matches:
    test = entry.split("|")
    if test[0] not in rules.keys():
        rules[test[0]] = Rule(test[0])
    rules[test[0]].add_before(test[1])
    if test[1] not in rules.keys():
        rules[test[1]] = Rule(test[1])
    rules[test[1]].add_after(test[0])

# rules_string = "\r\n".join(rules)
# df_rules = pd.read_table(io.StringIO(rules_string), header=None, sep="|", names=["before", "after"])
# before_rules = df_rules["before"].tolist()
# after_rules = df_rules["after"].tolist()
# print(df_rules)

lines = file_content.splitlines()


def check_full_line(_line, _rules):
    _x = _line.copy()
    _rules_kept = True
    for q in range(len(_line)):
        _x.remove(_line[q])
        if not rule_passing(_line[q], _x, _rules):
            _rules_kept = False
            break
    return _rules_kept


print("---------")
total = 0
reorder = []
for i in range(len(lines) - len(rule_matches)-1):
    check = lines[i+len(rule_matches)+1].split(",")
    # x = check.copy()
    rules_kept = check_full_line(check, rules)
    # rules_kept = True
    # for j in range(len(check)):
    #     x.remove(check[j])
    #     if not rule_passing(check[j], x, rules):
    #         rules_kept = False
    #         break
        # if check[i] in rules.keys():
        #     s1 = set(x)
        #     if rules[check[i]].after:
        #         s2 = set(rules[check[i]].after)
        #         if s1.intersection(s2):
        #             rules_kept = False
        #             break
        #     if rules[check[i]].before:
        #         s2 = set(rules[check[i]].after)
        #         if s1.intersection(s2):
        #             rules_kept = False
        #             break
    if rules_kept:
        total += int(check[len(check)//2])
    else:
        reorder.append(check)

print(total)
print(reorder)


total = 0
timeout = time.time() + 0.25
for attempt in reorder:
    # print("\n\nThis is an attempt for:")
    # print(attempt)
    passes = False
    for element in attempt:
        for i in range(len(attempt)):
            x = attempt.copy()
            x.remove(element)
            x.insert(i, element)
            # print(x, i, element)
            if check_full_line(x, rules):
                # print("It passes")
                passes = True
                total += int(x[len(x) // 2])
                break
        if passes:
            break
    while not passes:
        # print("Needs further correction")
        random_reorder = attempt.copy()
        random.shuffle(random_reorder)
        for element in random_reorder:
            for i in range(len(random_reorder)):
                x = random_reorder.copy()
                x.remove(element)
                x.insert(i, element)
                # print(x, i, element)
                if check_full_line(x, rules):
                    # print("It passes")
                    passes = True
                    total += int(x[len(x) // 2])
                    break


    # counter = 0
    # string_var = attempt.copy()
    # print(len(string_var))
    # if check_full_line(string_var, rules):
    #     total += int(string_var[len(string_var) // 2])
    #     break
    # else:
    #     index_to_move = 0
    # order = []
    # while counter < len(string_var):
    #     print(counter)
    #     if counter == index_to_move:
    #         order.append(index_to_move + 1)
    #         order.append(index_to_move)
    #         if len(order) < len(string_var):
    #             for fill in range(len(string_var) - len(order)):
    #                 order.append(fill + index_to_move + 2)
    #         string_var[:] = [string_var[new_pos] for new_pos in order]
    #         if check_full_line(string_var, rules):
    #             total += int(string_var[len(string_var) // 2])
    #             break
    #         else:
    #             index_to_move = 1
    #             counter = 0
    #     else:
    #         order.append(counter)
    #         counter += 1

    # passing = False
    # full_loop = 0
    # loop_end = len(attempt)
    # index_to_move = 0
    # x = attempt.copy()
    # stop_looping = loop_end
    # last_pos = len(attempt) - 1
    # order = []
    # for i in range(loop_end):
    #     order.append(i)
    # #print("initial order")
    # #print(order)
    # while not passing:
    #     #print(check_full_line(x, rules))
    #     #print("new check:")
    #     #print("original: " + ", ".join(x))
    #     x[:] = [x[new_pos] for new_pos in order]
    #     #print(order)
    #     print("new: " + ", ".join(x))
    #     if check_full_line(x, rules):
    #         print("It passed\n\n\n")
    #         # print(x)
    #         passing = True
    #     else:
    #         order = []
    #         counter = 0
    #         building = True
    #         while building:
    #             if counter == index_to_move:
    #                 print("counter and index match")
    #                 order.append(counter + 1)
    #                 order.append(counter)
    #                 index_to_move += 1
    #                 print(len(order))
    #                 print(len(attempt))
    #                 if len(order) <= len(attempt):
    #                     print("filling")
    #                     for fill in range(len(attempt) - len(order)):
    #                         order.append(fill + index_to_move + 1)
    #                     building = False
    #             else:
    #                 order.append(counter)
    #                 counter += 1
    #             if counter >= len(attempt):
    #                 print("no match found")
    #                 building = False
            # if index_to_move == 0:
            #     order.append(1)
            #     order.append(0)
            #     for i in range(loop_end - 2):
            #         order.append(i + 2)
            #     index_to_move += 1
            # elif index_to_move == 1:
            #     print("index to move is: " + str(index_to_move))
            #     order.append(0)
            #     order.append(2)
            #     order.append(1)
            #     if len(order) != loop_end:
            #         for i in range(loop_end - 2):
            #             order.append(i + 2)
            #     index_to_move += 1
            # else:
            #     print("generalising")
            #     print("index to move is: " + str(index_to_move))
            #     counter = 0
            #     building = True
            #     while building:
            #         if counter == index_to_move:
            #             order.append(counter + 1)
            #             order.append(counter)
            #             counter += 2
            #         else:
            #             order.append(counter)
            #             counter += 1
            #         if counter == len(attempt):
            #             building = False
                # for i in range(index_to_move):
                #     print("appending: " + str(i))
                #     order.append(i)
                # order.append(index_to_move + 1)
                # order.append(index_to_move)
                # print("appending: " + str(index_to_move))
                # for i in range(loop_end - index_to_move - 1):
                #     order.append(i + index_to_move)
                #     print("appending: " + str(i + index_to_move + 1))
                # index_to_move += 1
                # if index_to_move >= stop_looping:
                #     print("reset the loop")
                #     index_to_move = 0
                #     stop_looping -= 1

    #         print(order)
    # total += int(x[len(x) // 2])

print(total)


#
#
# for attempt in reorder:
#     print("Start of a trying to correct")
#     print(attempt)
#     x = attempt.copy()
#     passing = False
#     i = 0
#     while not passing:
#         test_value = x[i]
#         s1 = set(x)
#         # print(test_value)
#         if test_value in rules.keys():
#             if rules[test_value].after:
#                 s2 = set(rules[test_value].after)
#                 if s1.intersection(s2):
#                     # print("=======")
#                     # print(x)
#                     # print(s1.intersection(s2))
#                     # print(attempt[i])
#                     # print(s1)
#                     # print(s2)
#                     intersects = list(s1.intersection(s2))
#                     # print(intersects)
#                     orion = None
#                     for chuck in intersects:
#                         orion = attempt.index(chuck)
#                         # print(x.index(chuck))
#                     order = []
#                     # print("orion")
#                     # print(orion)
#                     if orion:
#                         for k in range(orion - 1):
#                             order.append(k)
#                         order.append(orion)
#                     order.append(i)
#                     start = len(order)
#                     for j in range(len(attempt) - start):
#                         order.append(j + start)
#                     # print("order = ")
#                     # print(order)
#                     x = []
#                     for value in order:
#                         x.append(attempt[value])
#                     # print(x)
#                     # print("Checking full line")
#                     # print(check_full_line(x, rules))
#                     if check_full_line(x, rules):
#                         passing = True
#                         print("It passes")
#                         print(x)
#                         break
#                     print(rule_passing(x[i], x, rules))
#                     # print("=======")
#                     rules_kept = False
#             if rules[test_value].before:
#                 # print("***************")
#                 s2 = set(rules[test_value].before)
#                 if s1.intersection(s2):
#                     intersects = list(s1.intersection(s2))
#                     orion = None
#                     for chuck in intersects:
#                         orion = attempt.index(chuck)
#                     order = []
#                     if orion:
#                         for k in range(orion - 1):
#                             order.append(k)
#                         order.append(orion)
#                     order.append(i)
#                     print("Before order")
#                     print(intersects)
#                     print(order)
#                     start = len(order)
#                     for j in range(len(attempt) - start):
#                         order.append(j + start)
#                     x = []
#                     for value in order:
#                         x.append(attempt[value])
#                     if check_full_line(x, rules):
#                         passing = True
#                         print("It passes")
#                         print(x)
#                         break
#                     rules_kept = False
#                     # print(s1.intersection(s2))
#             x.remove(test_value)
#         else:
#             print("this was OK")
#
