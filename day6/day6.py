#Get data from text file
data = open("day6/day6.txt", "r").read().split("\n")
#print(data)

race_seconds = data[0].split(":")[1].strip(" ")
race_seconds = race_seconds.split()

best_distance = data[1].split(":")[1].strip(" ")
best_distance = best_distance.split()

print(race_seconds)
print(best_distance)

way_to_beat_record = 0


counter = 0 
for race in race_seconds:

    race = int(race)
    time_to_beat = int(best_distance[counter])
    #print(type(race))
    
    number_beat = 0
    for i in range(1, race):
        race_distance = (race - i) * i
        #print(race_distance)
        if race_distance > time_to_beat:
            number_beat += 1
    
    print(number_beat)
    if counter == 0:
        way_to_beat_record += number_beat
        counter += 1
    else:
        way_to_beat_record = (way_to_beat_record * number_beat)
        counter += 1

    
        

print("Part 1: " + str(way_to_beat_record))

new_race = ""
for race in race_seconds:
    new_race += race
new_best_distance = ""
for distance in best_distance:
    new_best_distance += distance
new_race = int(new_race)
new_best_distance = int(new_best_distance)
way_to_beat_record_2 = 0
for i in range(1, new_race):
    race_distance = (new_race - i) * i
    
    if race_distance > new_best_distance:
        way_to_beat_record_2 += 1
    

print("Part 2: " + str(way_to_beat_record_2))