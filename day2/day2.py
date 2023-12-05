#Get data from text file
data = open("day2/day2.txt", "r").read().split("\n")


# More fun with strip / split https://medium.com/@Alexander_H/removing-characters-before-after-and-in-the-middle-of-strings-fb4930cce76a#:~:text=lstrip()%20%23strips%20everything%20before,set%20of%20characters%20you%20give.

sum = 0
sum_min = 0 

for i, game in enumerate(data):
    game = game.split(":")[1].split(";")
    #print(game)
    #create list to hold and check against values red, green, blue
    rgb = [0, 0, 0]
    game_possible = True
    for cubes_shown in game:
        cubes_shown = cubes_shown.strip( ).split(",")
        #print(cubes_shown)
        for cubes in cubes_shown:
            cubes = cubes.strip().split(" ")
            #print(cubes)

            if (((cubes[1]) == "red" and int(cubes[0]) > 12) or 
                ((cubes[1]) == "green" and int(cubes[0]) > 13) or 
                ((cubes[1]) == "blue" and int(cubes[0]) > 14)):
                game_possible = False
            if cubes[1] == "red" and int(cubes[0]) > rgb[0]:
                rgb[0] = int(cubes[0])
            if cubes[1] == "green" and int(cubes[0]) > rgb[1]:
                rgb[1] = int(cubes[0])
            if cubes[1] == "blue" and int(cubes[0]) > rgb[2]:
                rgb[2] = int(cubes[0])
    if game_possible:
        sum += (i + 1)
    sum_min += (rgb[0] * rgb[1] * rgb[2])

print("Part 1: " + str(sum))
print("Part 2: " + str(sum_min))

