from aoc import get_input

data = get_input(14).splitlines()

walls = set()
for line in data:
    edges = line.split(" -> ")
    for i in range(len(edges) - 1):
        start_x, start_y = [int(x) for x in edges[i].split(",")]
        end_x, end_y = [int(x) for x in edges[i + 1].split(",")]
        for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
            walls.add((x, start_y))
        for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
            walls.add((start_x, y))
wall_count = len(walls)
bottom = max(walls, key = lambda t: t[1])[1]
sand = None
while True:
    if sand is None:
        sand = (500, 0)

    if sand[1] > bottom:
        break
    elif (sand[0], sand[1] + 1) not in walls:
        sand = (sand[0], sand[1] + 1)
    elif (sand[0] - 1, sand[1] + 1) not in walls:
        sand = (sand[0] - 1, sand[1] + 1)
    elif (sand[0] + 1, sand[1] + 1) not in walls:
        sand = (sand[0] + 1, sand[1] + 1)
    else:
        walls.add(sand)
        sand = None
print(len(walls) - wall_count)
