from collections import deque


# time complexity: O(v+e) in general; 0(v) = O(length*width) in normal grid world w/ 4 neighbors; edges can be more than 4 here, but ok
# space complexity: O(v) = O(length*width)
def grid_with_portals_steps(g: list[list[str]]) -> int:
    """count steps to exit in grid g. S is start. E is exit. other letters are portals."""
    locations = {}
    seen = {}
    portals_seen = {}

    for i, row in enumerate(g):
        for j, value in enumerate(row):
            if value not in locations:
                locations[value] = [(i, j)]
            else:
                locations[value].append((i, j))

    print(locations)

    start_queue = deque([[loc, 0, "S"] for loc in locations["S"]])
    exit_queue = deque([[loc, 0, "E"] for loc in locations["E"]])
    queue = start_queue + exit_queue

    for loc in locations["S"]:
        seen[loc] = [0, "S"]
    for loc in locations["E"]:
        seen[loc] = [0, "E"]

    while queue:
        print()
        print("queue", queue)
        v = queue.popleft()
        print("v", v)

        neighbors = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        if g[v[0][0]][v[0][1]] not in portals_seen and g[v[0][0]][v[0][1]] not in ["S", "E", ".", "#"]:
            portals_seen[(v[0][0], v[0][1])] = True
            for loc in locations[g[v[0][0]][v[0][1]]]:
                neighbors.append([loc[0] - v[0][0], loc[1] - v[0][1]])

        for neighbor in neighbors:
            child = (v[0][0] + neighbor[0], v[0][1] + neighbor[1])
            if 0 <= child[0] < len(g) and 0 <= child[1] < len(g[0]):
                if v[2] == "S":
                    if child in seen and seen[child][1] == "E":
                        return seen[child][0] + v[1] + 1  # distance from E to child node + dist to v + 1
                    elif child not in seen and (("#" in locations and child not in locations["#"]) or "#" not in locations):
                        seen[(v[0][0] + neighbor[0], v[0][1] + neighbor[1])] = [v[1] + 1, "S"]
                        queue.append([(v[0][0] + neighbor[0], v[0][1] + neighbor[1]), v[1] + 1, "S"])

                else:
                    if child in seen and seen[child][1] == "S":
                        return seen[child][0] + v[1] + 1  # distance from E to child node + dist to v + 1
                    elif child not in seen and (("#" in locations and child not in locations["#"]) or "#" not in locations):
                        seen[(v[0][0] + neighbor[0], v[0][1] + neighbor[1])] = [v[1] + 1, "E"]
                        queue.append([(v[0][0] + neighbor[0], v[0][1] + neighbor[1]), v[1] + 1, "E"])
                        if child not in locations["."] and child not in locations["E"]:
                            for loc in locations[g[child[0]][child[1]]]:
                                if loc not in seen:
                                    queue.append([loc, v[1] + 2, "E"])

    return -1


print(grid_with_portals_steps([[".", "E", "."],
                         [".", "#", "E"],
                         [".", "S", "#"]]))

print(grid_with_portals_steps([["a", ".", "S", "a"],
                         ["#", "#", "#", "#"],
                         ["E", "b", ".", "b"]]))

print(grid_with_portals_steps([["a", "S", ".", "b"],
                         ["#", "#", "#", "#"],
                         ["E", "b", ".", "a"]]))

print(grid_with_portals_steps([["x", "S", ".", ".", "x", ".", ".", "E", "x"]]))

print(grid_with_portals_steps([["x", "E", "x", "x", "x"],
                               ["x", "x", ".", "x", "x"],
                               ["x", "x", "x", "x", "x"],
                               ["x", "x", "x", "S", "x"],
                               ["x", "x", "x", "x", "x"]]))







