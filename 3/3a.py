from aoc import get_input
import string

priorities = {}
for index, letter in enumerate(string.ascii_letters):
    priorities[letter] = index+1

data = get_input(3).splitlines()

sum = 0
for line in data:
    item1 = line[:len(line) // 2]
    item2 = line[len(line) // 2:]
    duplicate = set(item1).intersection(item2)
    sum += priorities[duplicate.pop()]
print(sum)