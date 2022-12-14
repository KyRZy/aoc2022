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

bottom = max(walls, key = lambda t: t[1])[1]
left = min(walls, key = lambda t: t[0])[0]
right = max(walls, key = lambda t: t[0])[0]

for y in range(bottom+1):
    for x in range(left,right+1):
        if (x,y) in walls:
            print("#",end="")
        else:
            print(".",end="")
    print("")

