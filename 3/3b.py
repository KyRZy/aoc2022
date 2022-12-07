from aoc import get_input
import string

priorities = {}
for index, letter in enumerate(string.ascii_letters):
    priorities[letter] = index+1

data = get_input(3).splitlines()

sum = 0
for i in range(0, len(data)-1, 3):
    backpack1 = data[i]
    backpack2 = data[i+1]
    backpack3 = data[i+2]
    duplicate = set(backpack1).intersection(backpack2).intersection(backpack3)
    sum += priorities[duplicate.pop()]
print(sum)