from aoc import get_input

data = get_input(1).splitlines()

max = current = 0
for line in data:
    if line != "":
        current += int(line)
        continue
    if current > max:
            max = current
    current = 0
print(max)