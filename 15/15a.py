from aoc import get_input
import re

data = get_input(15).splitlines()

row = 2000000
beacons = set()
empty = set()
for line in data:
    x1, y1, x2, y2 = [int(item) for item in re.findall(r"\d+", line)]
    if y2 == row:
        beacons.add((x2, y2))
    distance = abs(x1 - x2) + abs(y1 - y2)
    distance -= abs(row - y1)
    empty.update((x, row) for x in range(x1 - distance, x1 + distance + 1))

print(len(empty - beacons))
