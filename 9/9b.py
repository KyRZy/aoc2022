from aoc import get_input

data = get_input(9).splitlines()

positions = set()
rope = [(0, 0) for i in range(0, 10)]
def move(list, direction):
    for i in range(0, len(list)):
        if i == 0:
            if direction == "L":
                list[i] = list[i][0] - 1, list[i][1]
            if direction == "R":
                list[i] = list[i][0] + 1, list[i][1]
            if direction == "D":
                list[i] = list[i][0], list[i][1] - 1
            if direction == "U":
                list[i] = list[i][0], list[i][1] + 1
        elif abs(list[i][0] - list[i - 1][0]) == 2 or abs(list[i][1] - list[i - 1][1]) == 2:
            if list[i][1] == list[i - 1][1]:
                list[i] = list[i][0] + (1 if list[i][0] < list[i - 1][0] else -1), list[i][1]
            elif list[i][0] == list[i - 1][0]:
                list[i] = list[i][0], list[i][1] + (1 if list[i][1] < list[i - 1][1] else -1)
            else:
                list[i] = list[i][0] + (1 if list[i][0] < list[i - 1][0] else -1), list[i][1] + (1 if list[i][1] < list[i - 1][1] else -1)
    positions.add(list[-1])


for line in data:
    direction, value = line.split()

    for i in range(int(value)):
        move(rope,direction)
print(len(positions))
