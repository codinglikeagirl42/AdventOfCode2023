#Get data from text file
data = open("day4/day4.txt", "r").read().split("\n")

scratchcard_worth = 0
my_cards = [1] * (len(data))
#print(my_cards)
for i, cards in enumerate(data):
    cards = cards.split(":")[1].split("|")
    winning_numbers = cards[0].split()
    
    my_numbers = cards[1].split()

    card_worth = 0
    matching_numbers = 0
    for num in winning_numbers:
        if num in my_numbers:
            if card_worth == 0:
                card_worth += 1
                matching_numbers += 1
            else:
                card_worth = card_worth * 2
                matching_numbers += 1
    #print(matching_numbers)  
    if matching_numbers > 0:
        for num_cards in range(my_cards[i]) :
            for x in range(matching_numbers):
                my_cards[i + 1 + x] += 1
                #print(my_cards)
    scratchcard_worth += card_worth
        
print("Part 1: " + str(scratchcard_worth))
print("Part 2: " + str(sum(my_cards)))

