from aoc import get_input
import json
import functools

data = get_input(13).splitlines()

def validate(left, right) -> bool:
    if isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            result = validate(left[i], right[i])
            if result == 0:
                continue
            else:
                return result
        if len(left) == len(right):
            return 0
        else:
            return 1 if len(left) > len(right) else -1
    elif isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0
        elif left > right:
            return 1
        else:
            return -1
    elif isinstance(left, int):
        return validate([left], right)
    else:
        return validate(left, [right])


packages = [[[2]], [[6]]]
for line in data:
    if line != "":
        packages.append(json.loads(line))

packages = sorted(packages, key=functools.cmp_to_key(validate))
print((packages.index([[2]]) + 1) * (packages.index([[6]]) + 1))
