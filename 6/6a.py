from aoc import get_input
from collections import Counter

data = get_input(6).splitlines()

for i in range(0,len(data[0])-4):
    if(len(Counter(data[0][i:i+4])) == len(data[0][i:i+4])):
        print(i+4)
        print(data[0][i:i+4])
        break