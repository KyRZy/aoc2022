from aoc import get_input

def check_signal_strength(index, register):
    if index in [i for i in range(20, 230, 40)]:
        signal_strength_list.append(index * register)

data = get_input(10).splitlines()

signal_strength_list = []
counter = 0
register = 1
for line in data:
    inputs = line.split()
    if inputs[0] == "noop":
        counter += 1
        check_signal_strength(counter, register)
    elif inputs[0] == "addx":
        for i in range(0, 2):
            counter += 1
            check_signal_strength(counter, register)
        register += int(inputs[1])
print(sum(signal_strength_list))