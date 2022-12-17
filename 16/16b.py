# WORK IN PROGRESS

from aoc import get_input
import re
import copy
from itertools import product

data = get_input(16).splitlines()

data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".splitlines()

valves = {}
class Valve:
    def __init__(self, name, rate, tunnels_to):
        self.name = name
        self.rate = rate
        self.tunnels_to = tunnels_to

class TwoPaths:
    def __init__(self):
        self.time = 0
        self.paths = [("AA","AA")]
        self.pressure = 0
        self.opened_valves = set()

for line in data:
    v = re.findall(r"[A-Z]{2}", line)
    rate = re.findall(r"\d+",line)[0]
    valve = Valve(v[0], int(rate), v[1:])
    valves[valve.name] = valve

queue = [TwoPaths()]
checked = []
best = queue[0]
MAX_TIME = 26
while queue:
    current = queue[0]
    queue = queue[1:]

    print(len(queue), current.time)

    current_state = (sorted(current.paths[-1]), current.pressure)
    if current_state in checked:
        continue
    checked.append(current_state)

    if current.time >= MAX_TIME:
        continue

    actions = []
    for node in current_state[0]:
        actions.append([])
        if node not in current.opened_valves and valves[node].rate > 0:
            actions[-1].append(("open",node))

        for path in valves[node].tunnels_to:
            actions[-1].append(("move",path))

    all_combinations = set(product(*actions))

    for combination in all_combinations:
        next_step = copy.deepcopy(current)
        next_step.time += 1

        if combination[0][0] == combination[1][0] == "open" and combination[0][1] == combination[1][1]:
            continue

        for action in combination:
            if action[0] == "open":
                next_step.opened_valves.add(node)
                next_step.pressure += (MAX_TIME - current.time) * valves[node].rate

        next_step.paths.append((combination[0][1], combination[1][1]))

        if best.pressure < next_step.pressure:
            best = next_step

        queue.append(next_step)

print(best.time)
print(best.pressure)
print(best.paths)
