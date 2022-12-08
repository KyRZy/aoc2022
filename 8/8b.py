from aoc import get_input


def get_column(matrix, i):
    return [row[i] for row in matrix]


data = get_input(8).splitlines()

forest = [[int(x) for x in line] for line in data]

max_scenic = 0
for x in range(1, len(forest) - 1):
    for y in range(1, len(forest[x]) - 1):
        height = forest[x][y]
        current_scenic = 1
        # check left
        direction_score = 0
        for i in range(y - 1, -1, -1):
            direction_score += 1
            if forest[x][i] < height:
                continue
            break

        current_scenic *= direction_score
        # check right
        direction_score = 0
        for i in range(y + 1, len(forest[x])):
            direction_score += 1
            if forest[x][i] < height:
                continue
            break

        current_scenic *= direction_score

        column = get_column(forest, y)
        # check up
        direction_score = 0
        for i in range(x - 1, -1, -1):
            direction_score += 1
            if column[i] < height:
                continue
            break

        current_scenic *= direction_score
        # check down
        direction_score = 0
        for i in range(x + 1, len(column)):
            direction_score += 1
            if column[i] < height:
                continue
            break

        current_scenic *= direction_score

        if max_scenic < current_scenic:
            max_scenic = current_scenic
print(max_scenic)
