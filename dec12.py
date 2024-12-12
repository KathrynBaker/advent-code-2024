# https://adventofcode.com/2024/day/12

simple_example = """
AAAA
BBCD
BBCC
EEEC
"""

simple_example = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""


class plot_region:
    def __init__(self, region_name, row, col):
        self.region_name = region_name
        self.area = 1
        self.perimeter = 4
        self.locations = {(row, col)}

    def add_to_area(self, row, col):
        matches = self.locations.intersection({(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)})
        print(self.locations.intersection(matches))
        self.locations.add((row, col))
        print(len(matches))
        self.area = self.area + 1
        if len(matches) == 0:
            self.perimeter = self.perimeter + 4
        if len(matches) == 1:
            self.perimeter = self.perimeter + 2

    def __str__(self):
        return f"Region {self.region_name}: Area = {self.area}; Perimeter = {self.perimeter}"

    def calculate_price(self):
        return self.area*self.perimeter

dict_plot = {}

simple_example = simple_example.split("\n")

for row_index in range(len(simple_example)):
    print(simple_example[row_index])
    row = simple_example[row_index]
    for column_index in range(len(row)):
        if row[column_index] in dict_plot.keys():
            dict_plot[row[column_index]].add_to_area(row_index, column_index)
        else:
            dict_plot[row[column_index]] = plot_region(row[column_index], row_index, column_index)

cost = 0
for item in dict_plot.keys():
    print(dict_plot[item])
    cost += dict_plot[item].calculate_price()

print(cost)

"""
This isn't quite working at the moment, I need to deal with discontiguous regions, this is 
probably most easily done by adding a number of regions, and making the locations lists
multi-dimensional, the set aspect may still just work 
"""
