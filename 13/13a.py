from aoc import get_input
import json

data = get_input(13).splitlines()

def validate(left, right) -> bool:
    if isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            result = validate(left[i], right[i])
            if result is None:
                continue
            else:
                return result
        if len(left) == len(right):
            return None
        else:
            return len(left) < len(right)
    elif isinstance(left, int) and isinstance(right, int):
        return left < right if left != right else None
    elif isinstance(left, int):
        return validate([left], right)
    else:
        return validate(left, [right])


pair_index = 0
sum_of_pair_indexes = 0
for i in range(0, len(data), 3):
    pair_index += 1
    first = json.loads(data[i])
    second = json.loads(data[i + 1])

    result = validate(first, second)
    if result or result is None:
        sum_of_pair_indexes += pair_index

print(sum_of_pair_indexes)
