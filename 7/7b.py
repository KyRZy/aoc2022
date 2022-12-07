from aoc import get_input

class NodeTree:
    def __init__(self, name):
        self.parent: NodeTree = None
        self.children_nodes: list[NodeTree] = []
        self.size: int = 0
        self.name: str = name

    def __str__(self):
        return f"{self.name} {self.size}"

def calculate_size(node: NodeTree, dir_sizes: list[NodeTree]) -> (int, list[NodeTree]):
    dir_size = 0
    for child in node.children_nodes:
        if child.size == 0:
            dir_size += calculate_size(child, dir_sizes)[0]
        else:
            dir_size += child.size

    node = NodeTree(node.name)
    node.size = dir_size
    dir_sizes.append(node)

    return dir_size, dir_sizes


tree = NodeTree("/")

data = get_input(7).splitlines()

current_node = tree
for line in data:
    if line.startswith("$ ls"):
        continue
    elif line.startswith("$ cd"):
        path = line[5:]
        if path == '/':
            current_node = tree
        elif path == "..":
            current_node = current_node.parent
        else:
            parent = current_node
            current_node = next(x for x in current_node.children_nodes if x.name == path)
            current_node.parent = parent
    elif line.startswith("dir"):
        path = line[4:]
        directory = NodeTree(path)
        current_node.children_nodes.append(directory)
    else:
        size, filename = line.split()
        file = NodeTree(filename)
        file.size = int(size)
        current_node.children_nodes.append(file)
currently_taken_space, dir_sizes = calculate_size(tree, [])
print(f"Current taken space = ", currently_taken_space)
print("Current free space =", 70000000 - currently_taken_space)
space_to_free = 30000000 - (70000000 - currently_taken_space)
print("Need to free =", space_to_free)
dir_sizes.sort(key=lambda x: x.size)
result = next(x for x in dir_sizes if x.size >= space_to_free)
print(result)