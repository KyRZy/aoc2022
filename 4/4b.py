from aoc import get_input
import re

data = get_input(4).splitlines()

amountOfPairs = 0
for line in data:
    (elf1start, elf1end, elf2start, elf2end) = [int(s) for s in re.split(',|-', line)]
    if (
            (elf1start <= elf2start <= elf1end) or (elf1start <= elf2end <= elf1end) or
            (elf2start <= elf1start <= elf2end) or (elf2start <= elf1end <= elf2end)
        ):
        amountOfPairs += 1
print(amountOfPairs)