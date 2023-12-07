#Get data from text file
data = open("day3/day3.txt", "r").read().split("\n")

my_number = ""
sum = 0

# I hate mapping pulling from last year
# Break statements - https://www.geeksforgeeks.org/python-break-statement/

#total rows and columns
x_total = len(data)
y_total = len(data[0])

for x in range(0, x_total):
    for y in range(0, y_total):
        current_position = data[x][y]

        if current_position == "*" or y == y_total - 1:
            
            y_start = max(0, y - 1)
            y_end = min(y_total - 1, y + 1)
            x_start = max(0, x - 1)
            x_end = min(x_total - 1, x + 1)
                
            numbers = []  
            for yy in range(y_start, y_end + 1):
                for xx in range(x_start, x_end + 1):

                            
                    if data[xx][yy].isnumeric:
                        #sum += (int(my_number[0]) * int(my_number[1]))
                        
                        
                                
                        
         

print("Part 2: " + str(sum))
