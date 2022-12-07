from aoc import get_input
import time

start_time = time.time()

data = get_input(2).splitlines()
shapeScore = { 'X' : 1,'Y' : 2,'Z' : 3,}
outcomeScore = {
    'A' : { 'X' : 3,'Y' : 6,'Z' : 0,},
    'B' : { 'X' : 0,'Y' : 3,'Z' : 6,},
    'C' : { 'X' : 6,'Y' : 0,'Z' : 3,}
}
stategy = {
    'X': {'A': 'Z', 'B': 'X', 'C': 'Y', },
    'Y': {'A': 'X', 'B': 'Y', 'C': 'Z', },
    'Z': {'A': 'Y', 'B': 'Z', 'C': 'X', },
}
sum = 0
for line in data:
    opponent, player = line.split()
    playerChoice = stategy[player][opponent]
    sum += shapeScore[playerChoice] + outcomeScore[opponent][playerChoice]

print(sum)
print("--- %s seconds ---" % (time.time() - start_time))