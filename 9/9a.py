from aoc import get_input

data = get_input(9).splitlines()

positions = set()

H = 0, 0
T = 0, 0
for line in data:
    direction, value = line.split()

    for i in range(int(value)):
        if direction == "L":
            H = H[0] - 1, H[1]
        if direction == "R":
            H = H[0] + 1, H[1]
        if direction == "D":
            H = H[0], H[1] - 1
        if direction == "U":
            H = H[0], H[1] + 1
        if abs(H[0] - T[0]) == 2 or abs(H[1] - T[1]) == 2:
            if H[1] == T[1]:
                T = T[0] + (1 if H[0] > T[0] else -1), T[1]
            elif H[0] == T[0]:
                T = T[0], T[1] + (1 if H[1] > T[1] else -1)
            else:
                T = T[0] + (1 if H[0] > T[0] else -1), T[1] + (1 if H[1] > T[1] else -1)
        positions.add(T)
print(len(positions))
