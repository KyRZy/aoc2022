from aoc import get_input
import re
import heapq
import copy

data = get_input(16).splitlines()

valves = {}
class Valve:
    def __init__(self, name, rate, tunnels_to):
        self.name = name
        self.rate = rate
        self.tunnels_to = tunnels_to

class PossiblePath:
    def __init__(self):
        self.time = 0
        self.path = ["AA"]
        self.pressure = 0
        self.opened_valves = set()

for line in data:
    v = re.findall(r"[A-Z]{2}", line)
    rate = re.findall(r"\d+",line)[0]
    valve = Valve(v[0], int(rate), v[1:])
    valves[valve.name] = valve

queue = [PossiblePath()]
checked = []
best = queue[0]
MAX_TIME = 30
while queue:
    current = queue[0]
    queue = queue[1:]

    current_state = (current.path[-1], current.pressure)
    if current_state in checked:
        continue
    checked.append(current_state)

    if current.time >= MAX_TIME:
        continue

    if current_state[0] not in current.opened_valves and valves[current_state[0]].rate > 0:
        current.time += 1
        current.opened_valves.add(current_state[0])
        current.pressure += (MAX_TIME - current.time) * valves[current_state[0]].rate
    for path in valves[current_state[0]].tunnels_to:
        next_step = copy.deepcopy(current)
        next_step.time += 1
        next_step.path.append(path)

        if best.pressure < next_step.pressure:
            best = next_step

        queue.append(next_step)
    print(len(queue), current.time)

print(best.time)
print(best.pressure)
print(best.path)
