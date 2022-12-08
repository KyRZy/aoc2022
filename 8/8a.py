from aoc import get_input


def get_column(matrix, i):
    return [row[i] for row in matrix]


data = get_input(8).splitlines()
forest = []

for line in data:
    forest.append([int(x) for x in line])

visible = 2 * len(forest) + 2 * len(forest[0]) -4
for x in range(1, len(forest) - 1):
    for y in range(1, len(forest[x]) - 1):
        height = forest[x][y]
        # check left
        if all(tree < height for tree in forest[x][:y]):
            visible += 1
            continue
        # check right
        if all(tree < height for tree in forest[x][y+1:]):
            visible += 1
            continue
        column = get_column(forest,y)
        # check up
        if all(tree < height for tree in column[:x]):
            visible += 1
            continue
        # check down
        if all(tree < height for tree in column[x+1:]):
            visible += 1
            continue
print(visible)
