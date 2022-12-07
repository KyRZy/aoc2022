from aoc import get_input

data = get_input(1).splitlines()

max1 = max2 = max3 = current = 0
for line in data:
    if line != "":
        current += int(line)
        continue
    if current > max1:
        max3 = max2
        max2 = max1
        max1 = current
    elif current > max2:
        max3 = max2
        max2 = current
    elif current > max3:
        max3 = current
    current = 0
print(max1 + max2 + max3)