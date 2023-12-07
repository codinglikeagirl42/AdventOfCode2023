# Import Pandas as PD
import pandas as pd

#Get data from text file
data = open("day7/test.txt", "r").read().split("\n")

# A, K, Q, J, T, 9...
# 5 of a kind - 4 of a kind - Full House (3 of a kind + 2 of a kind) - 3 of a kind - 2 Pair (2 - 2of a kind) - 2 of a kind - High Card (all different)

camel_card_hands = pd.DataFrame(data)
#create a dataframe
