#Get data from text file
data = open("day3/day3.txt", "r").read().split("\n")

my_number = ""
sum = 0

special_char = "[@_!#$%^&*()<>?/\|}{~:+-]"

# I hate mapping pulling from last year
# Break statements - https://www.geeksforgeeks.org/python-break-statement/

#total rows and columns
x_total = len(data)
y_total = len(data[0])
sympols = ['*', '=', '/', '%', '#', '&', '$', '-', '@', '+']

for x in range(0, x_total):
    for y in range(0, y_total):
        current_position = data[x][y]

        #if not current_position.isnumeric() and current_position not in sympols:
            #sympols.append(current_position)
    
        if current_position.isnumeric():
            #print(data[x][y])
            my_number += data[x][y]
            #print(my_number)


        if current_position in sympols or current_position == "." or y == y_total - 1:
            if len(my_number) > 0:
                y_start = max(0, y - len(my_number) - 1)
                y_end = min(y_total - 1, y)
                x_start = max(0, x - 1)
                x_end = min(x_total - 1, x + 1)
                
                done = False
                for yy in range(y_start, y_end + 1):
                    for xx in range(x_start, x_end + 1):
                        # must also check for .
                        if (data[xx][yy] in sympols and data[xx][yy] != "."):
                            sum += int(my_number)
                            #print(my_number)
                            my_number = ""
                            done = True
                            break
                    if done == True:
                        break
                my_number = ""

print("Part 1: " + str(sum))



