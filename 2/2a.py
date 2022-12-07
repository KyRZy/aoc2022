from aoc import get_input

data = get_input(2).splitlines()
shapeScore = { 'X' : 1,'Y' : 2,'Z' : 3,}
outcomeScore = {
    'A' : { 'X' : 3,'Y' : 6,'Z' : 0,},
    'B' : { 'X' : 0,'Y' : 3,'Z' : 6,},
    'C' : { 'X' : 6,'Y' : 0,'Z' : 3,}
}
sum = 0
for line in data:
    opponent, player = line.split()
    sum += shapeScore[player]+ outcomeScore[opponent][player]

print(sum)