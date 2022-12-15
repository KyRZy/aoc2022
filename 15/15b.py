from aoc import get_input
import re
from z3 import *

data = get_input(15).splitlines()

solver = Solver()
x = Int("x")
y = Int("y")
solver.add(x >= 0, y >= 0, x <= 4000000, y <= 4000000)

for line in data:
    x1, y1, x2, y2 = [int(item) for item in re.findall(r"\d+", line)]
    distance = abs(x1 - x2) + abs(y1 - y2)
    solver.add(Abs(x1 - x) + Abs(y1 - y) > distance)

print(solver.check())
model = solver.model()
print(model[x].as_long() * 4000000 + model[y].as_long())
