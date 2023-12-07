#Get data from text file
data = open("day3/test.txt", "r").read().split("\n")

my_number = []
sum = 0

special_char = '[@_!#$%^&*()<>?/\|}{~:+-]'

# I hate mapping pulling from last year

#total rows and columns
x_total = len(data)
y_total = len(data[0])


for x in range(0, x_total):
    for y in range(0, y_total):
        if data[x][y].isnumeric():
            my_number.append(data[x][y])
        if data[x][y] in special_char or y == y_total - 1:
            if len(my_number) > 0:
                y_start = max(0, y - (len(my_number)) - 1)
                y_end = min(y_total -1, y)
                x_start = max(0, x-1)
                x_end = min(x_total - 1, x+1)
            for yy in range(y_start, y_end + 1):
                for xx in range(x_start, x_end+1):
                    if (data[xx][yy] != "." and not data[xx][yy].isnumeric()):
                        sum += int("".join(my_number))
                        my_number = []
            my_number =[]
print(sum)



