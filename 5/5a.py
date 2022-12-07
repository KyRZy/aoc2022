from aoc import get_input
import  re

data = get_input(5).splitlines()
graph = []
graphParsed = False
for index, line in enumerate(data):
    if line == "" and not graphParsed:
        columnAmount = int(data[index-1].split()[-1])
        for i in range(0, columnAmount):
            graph.append([])
        for i in range(index-2, -1, -1):
            for crate in re.finditer(r"\w", data[i]):
                graph[int(crate.start() // 4)].append(crate.group(0))
        graphParsed = True
    elif graphParsed:
        moves, cratesFrom, cratesTo = [int(s) for s in re.findall(r"\d+", line)]
        for i in range(0, int(moves)):
            graph[int(cratesTo)-1].append(graph[int(cratesFrom)-1].pop())
for stack in graph:
    print(stack[-1], end="")

