#Get data from text file
data = open("day1/day1.txt", "r").read().split("\n")
callabration_sum = 0

for line in data:
    callibration = []
    
    for l in line:
        if l.isnumeric() == True:
            callibration.append(l)
    #print(callibration)
    callibration_number = int(callibration[0] + callibration[-1])
    callabration_sum += callibration_number
print("Part 1: " + str(callabration_sum))

# For part 2 used the enumerate function in python.
# More inforamtion can be found here: https://www.geeksforgeeks.org/enumerate-in-python/
# creat a list of written numbers
written_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
callibration_sum_two = 0
for line in data:
    callibration_two = []
    # loop thru all characters in each line by i(index)
    for i, char in enumerate(line):
        # loop thru written_numbers by index value(value)
        for value, number in enumerate(written_numbers):
            # if a written number is found add its value to our list
            if number in line[i:i+len(number)]:
                # add 1 to the index(value) to account for no zero
                #alternitivly you could add zero to the list
                callibration_two.append(str(value + 1))
        if char.isnumeric() == True:
            callibration_two.append(char)
    callibration_number_two = int(callibration_two[0] + callibration_two[-1])
    callibration_sum_two += callibration_number_two
print("Part 2: " + str(callibration_sum_two))