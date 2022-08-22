# dequeue with popleft() will only take constant time, not linear time like .pop(0) on lists
from collections import deque

print("Graphs where edges are represented as adjacency lists can be more efficient than graphs with an adjacency matrix")
print("The space of adjacency matrix and the time to search through it to find neighbor nodes can be significant")
print("This is especially important when the graph connections between the vertices are sparse.")

print("let's look at a directed graph.")

graph = {5: [3, 7],
         3: [2, 4],
         7: [8],
         2: [],
         4: [8],
         8: []}


def bfs(graph_input: dict = graph, node: int = 5) -> None:
    queue = deque([node])
    seen = {}

    print("pop(left off queue), check (if vertex not seen), process (by just printing)")
    while queue:
        v = queue.popleft()
        print("pop and check", v)
        if not seen.get(v, False):
            seen[v] = True
            print("process", v)
            for neighbor in graph_input[v]:
                queue.append(neighbor)


def dfs(graph_input: dict = graph, node: int = 5) -> None:
    stack = [node]
    seen = {}

    while stack:
        v = stack.pop()
        print("pop and check", v)
        if not seen.get(v, False):
            seen[v] = True
            print("process", v)
            for neighbor in graph_input[v]:
                stack.append(neighbor)


def bidirectional_bfs(graph_input: dict = graph, start_node: int = 5, end_node: int = 7):
    g = graph_input
    v = start_node
    w = end_node


print("Breadth First Search")
bfs()
print("Depth First Search")
dfs()

print("For bidirectional BFS, see grid_with_portals.py")


