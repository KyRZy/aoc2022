from aoc import get_input
from collections import Counter

data = get_input(6).splitlines()

for i in range(0,len(data[0])-14):
    if(len(Counter(data[0][i:i+14])) == len(data[0][i:i+14])):
        print(i+14)
        print(data[0][i:i+14])
        break