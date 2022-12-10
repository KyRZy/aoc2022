from aoc import get_input
def draw(index, register):
    if abs((index % 40) - register) < 2:
        print("#",end="")
    else:
        print(".",end="")

    if (index + 1) % 40 == 0:
        print("")

data = get_input(10).splitlines()

counter = 0
register = 1
for line in data:
    inputs = line.split()
    if inputs[0] == "noop":
        draw(counter, register)
        counter += 1
    elif inputs[0] == "addx":
        for i in range(0,2):
            draw(counter, register)
            counter += 1
        register += int(inputs[1])