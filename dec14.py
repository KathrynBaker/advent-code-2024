import parse
import os
from collections import Counter

day = 14
use_example = False


def get_file_path(day_to_use, example):
    if example:
        return os.path.join("example_inputs", "dec" + str(day_to_use) + "_input_example.txt")
    else:
        return os.path.join("inputs", "dec" + str(day_to_use) + "_input.txt")


class Robot:
    def __init__(self, info):
        format_string = "p={pcol},{prow} v={mcol},{mrow}"
        data = parse.parse(format_string,info)
        self.col = int(data["pcol"])
        self.row = int(data["prow"])
        self.move_col = int(data["mcol"])
        self.move_row = int(data["mrow"])
        self.max_col = 100
        self.max_row = 102
        self.quad = "INIT"
        self.set_quad()

    def __str__(self):
        return f"p={self.col},{self.row}, quad={self.quad}"

    def move_bot(self):
        if 0 <= self.col + self.move_col <= self.max_col:
            self.col = self.col + self.move_col
        elif self.col + self.move_col < 0:
            self.col = self.max_col + 1 + self.col + self.move_col
        else:
            self.col = self.col + self.move_col - self.max_col - 1
        if 0 <= self.row + self.move_row <= self.max_row:
            self.row = self.row + self.move_row
        elif self.row + self.move_row < 0:
            self.row = self.max_row + 1 + self.row + self.move_row
        else:
            self.row = self.row + self.move_row - self.max_row - 1
        self.set_quad()

    def set_quad(self):
        if self.row == self.max_row/2 or self.col == self.max_col/2:
            self.quad = "N"
        elif self.row < self.max_row/2 and self.col < self.max_col/2:
            self.quad = "A"
        elif self.row < self.max_row / 2 and self.col > self.max_col / 2:
            self.quad = "B"
        elif self.row > self.max_row / 2 and self.col < self.max_col / 2:
            self.quad = "C"
        elif self.row > self.max_row / 2 and self.col > self.max_col / 2:
            self.quad = "D"
        else:
            self.quad = "ERROR"


with open(get_file_path(day, use_example), "r") as file:
    file_content = file.read()

entries = file_content.split("\n")

robots = []
for line in entries:
    robots.append(Robot(line))

# print("My bots")
# for bot in robots:
#     print(bot)

for i in range(100):
    for robot in robots:
        robot.move_bot()

quads = []
for robot in robots:
    quads.append(robot.quad)

count = Counter(quads)

print(count["A"] * count["B"] * count["C"] * count["D"])
