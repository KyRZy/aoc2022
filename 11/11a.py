from aoc import get_input
import re

data = get_input(11).splitlines()

class Monkey:
    def __init__(self):
        self.items = []
        self.operation_sign = ""
        self.operation_value = ""
        self.divisible_by = 0
        self.throw_to_if_true = None
        self.throw_to_if_false = None
        self.inspected = 0

monkeys = []
for i in range(0,len(data),7):
    monkey = Monkey()
    monkey.items = [int(item) for item in re.findall(r"\d+", data[i + 1])]
    operation = data[i + 2].split()
    monkey.operation_sign = operation[-2]
    monkey.operation_value = operation[-1]
    monkey.divisible_by = int(data[i + 3].split()[-1])
    monkey.throw_to_if_true = int(data[i + 4].split()[-1])
    monkey.throw_to_if_false = int(data[i + 5].split()[-1])
    monkeys.append(monkey)

for _ in range(0,20):
    for monkey in monkeys:
        monkey.inspected += len(monkey.items)
        for item in monkey.items:
            modify_worry_level_by = int(monkey.operation_value) if monkey.operation_value != "old" else item
            worry_level = item
            match monkey.operation_sign:
                case "+":
                    worry_level += modify_worry_level_by
                case "*":
                    worry_level *= modify_worry_level_by
            worry_level //= 3
            if worry_level % monkey.divisible_by == 0:
                monkeys[monkey.throw_to_if_true].items.append(worry_level)
            else:
                monkeys[monkey.throw_to_if_false].items.append(worry_level)
        monkey.items = []

monkeys.sort(key=lambda x: x.inspected)
print(monkeys[-1].inspected * monkeys[-2].inspected)