# https://adventofcode.com/2024/day/5
import re
import pandas as pd
import io


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


with open("dec5_input_example.txt", "r") as file:
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


for attempt in reorder:
    print("Start of a trying to correct")
    print(attempt)
    x = attempt.copy()
    kanaka = attempt.copy()
    passing = False
    i = 0
    while not passing:
        test_value = x[i]
        s1 = set(x)
        # print(test_value)
        if x[i] in rules.keys():
            if rules[x[i]].after:
                s2 = set(rules[x[i]].after)
                if s1.intersection(s2):
                    # print("=======")
                    # print(x)
                    # print(s1.intersection(s2))
                    # print(attempt[i])
                    # print(s1)
                    # print(s2)
                    intersects = list(s1.intersection(s2))
                    # print(intersects)
                    orion = None
                    for chuck in intersects:
                        orion = attempt.index(chuck)
                        # print(x.index(chuck))
                    order = []
                    # print("orion")
                    # print(orion)
                    if orion:
                        for k in range(orion - 1):
                            order.append(k)
                        order.append(orion)
                    order.append(i)
                    start = len(order)
                    for j in range(len(attempt) - start):
                        order.append(j + start)
                    # print("order = ")
                    # print(order)
                    x = []
                    for value in order:
                        x.append(attempt[value])
                    # print(x)
                    # print("Checking full line")
                    # print(check_full_line(x, rules))
                    if check_full_line(x, rules):
                        passing = True
                        print("It passes")
                        print(x)
                        break
                    # print(rule_passing(x[i], x, rules))
                    # print("=======")
                    rules_kept = False
            if rules[x[i]].before:
                # print("***************")
                s2 = set(rules[x[i]].before)
                if s1.intersection(s2):
                    intersects = list(s1.intersection(s2))
                    orion = None
                    for chuck in intersects:
                        orion = attempt.index(chuck)
                    order = []
                    if orion:
                        for k in range(orion - 1):
                            order.append(k)
                        order.append(orion)
                    order.append(i)
                    start = len(order)
                    for j in range(len(attempt) - start):
                        order.append(j + start)
                    print("kanaka")
                    print(order)
                    kanaka = []
                    for value in order:
                        kanaka.append(attempt[value])
                    print(kanaka)
                    if check_full_line(kanaka, rules):
                        passing = True
                        print("It passes")
                        print(x)
                        break
                    rules_kept = False
                    # print(s1.intersection(s2))
            x.remove(test_value)
            i += 1
        else:
            print("this was OK")

