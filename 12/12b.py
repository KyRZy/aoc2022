import sys

from aoc import get_input
def neighbours(coords: tuple[int,int]):
    return [(coords[0] - 1, coords[1]),
            (coords[0] + 1, coords[1]),
            (coords[0], coords[1] + 1),
            (coords[0], coords[1] - 1)]

def findLetter(data: list[str], letter: str):
    for index, line in enumerate(data):
        if letter in line:
            return line.index(letter), index
def findAllAs(data: list[str]):
    result = []
    for index, line in enumerate(data):
        for letter in line:
            if letter == "a":
                result.append((line.index(letter), index))
    return result

def valid_height(data: list[str], current: tuple[int,int], neighbour: tuple[int,int]) -> bool:
    current_height = data[current[1]][current[0]]
    if current_height == "S":
        current_height = "a"
    neighbour_height = data[neighbour[1]][neighbour[0]]
    if neighbour_height == "E":
        neighbour_height = "z"
    return ord(neighbour_height) - ord(current_height) <= 1


data = get_input(12).splitlines()
min_path_len = sys.maxsize

end = findLetter(data, "E")
all_as = findAllAs(data)
for index, a in enumerate(all_as):
    print(index, len(all_as))
    start = a

    locations_to_check = [start]
    previous_locations = {start: None}

    while locations_to_check:
        current = locations_to_check[0]
        locations_to_check = locations_to_check[1:]

        if data[current[1]][current[0]] == "E":
            break

        for neighbour in neighbours(current):
            if 0 <= neighbour[0] <= len(data[0]) - 1 \
                    and 0 <= neighbour[1] <= len(data) - 1 \
                    and valid_height(data, current, neighbour) \
                    and neighbour not in previous_locations:
                locations_to_check.append(neighbour)
                previous_locations[neighbour] = current
    if current != end:
        continue

    path = []
    while current != start:
        path.append(current)
        current = previous_locations[current]

    path_len = len(path)
    if path_len < min_path_len:
        min_path_len = path_len
print(min_path_len)
