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
print("Part 1:" + callabration_sum)
 