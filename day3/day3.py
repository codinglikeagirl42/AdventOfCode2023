#Get data from text file
data = open("day3/day3.txt", "r").read().split("\n")

my_number = ""

# I hate mapping pulling from last year
# https://github.com/codinglikeagirl42/AdventOfCode2022/blob/day8/Day8/day8part1.py

#total rows and columns
x_total = len(data)
y_total = len(data[0])

