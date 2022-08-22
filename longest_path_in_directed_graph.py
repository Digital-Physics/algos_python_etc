# time complexity:
# space complexity:
def longest_path(l: list[int]) -> int:
    """each node has only one outgoing node. you can choose where to start.
    (e.g. [4, 3, 5, 1, 2]: 1 goes to 4, 2 goes to 3, 3 goes to 5, 4 goes to 1, 5 to 2
     -> 3; 3=>5=>2)"""
    print()
    print("*******************")
    print("start; input", l)
    after_n_steps = [j for j in range(len(l))]  # index is +1 in problem relative to Python list index
    seen_starting_from_j = [{j: True} for j in range(len(l))]
    stop_counting = [False for _ in range(len(l))]
    total_seen = [1 for _ in range(len(l))]

    for i in range(len(l)):  # row of next steps, etc.
        previous_step = after_n_steps[:]
        previous_total = total_seen[:]
        print()
        print(f"after {i} steps", after_n_steps)
        print(seen_starting_from_j)
        print(stop_counting)
        print(total_seen)
        for j in range(len(l)):
            after_n_steps[j] = l[previous_step[j]] - 1
            if stop_counting[j] or after_n_steps[j] in seen_starting_from_j[j]:
                stop_counting[j] = True
            else:
                seen_starting_from_j[j][after_n_steps[j]] = True
            total_seen[j] = previous_total[j] + 1 if not stop_counting[j] else previous_total[j]

    return max(total_seen)


def getMaxVisitableWebpages(N: int, L: list[int]) -> int:
    # Write your code here
    after_n_steps = [j for j in range(len(L))]
    seen_starting_from_j = [{j: True} for j in range(len(L))]
    stop_counting = [False for _ in range(len(L))]
    total_seen = [1 for _ in range(len(L))]

    for i in range(len(L)):
        previous_step = after_n_steps[:]
        previous_total = total_seen[:]

        for j in range(len(L)):
            after_n_steps[j] = L[previous_step[j]] - 1
            if stop_counting[j] or after_n_steps[j] in seen_starting_from_j[j]:
                stop_counting[j] = True
            else:
                seen_starting_from_j[j][after_n_steps[j]] = True
            total_seen[j] = previous_total[j] + 1 if not stop_counting[j] else previous_total[j]

    return max(total_seen)


def longest_path2(l: list[int]) -> int:
    """each node has only one outgoing node. you can choose where to start.
    (e.g. [4, 3, 5, 1, 2]: 1 goes to 4, 2 goes to 3, 3 goes to 5, 4 goes to 1, 5 to 2
     -> 3; 3=>5=>2)"""
    print()
    print("*******************")
    print("start; input", l)
    to_check_set = {j for j in range(len(l))}  # index is +1 in problem relative to Python list index
    distance_dict = {j: 0 for j in range(len(l))}
    max_dist = float("-inf")
    curr_node = 0

    while to_check_set:
        print("start_node", curr_node)
        curr_path_dict = {}
        curr_path = []
        count = 0
        print(curr_node not in curr_path_dict, curr_node in to_check_set)
        while curr_node not in curr_path_dict and curr_node in to_check_set:
            to_check_set.remove(curr_node)
            print("curr_node", curr_node)
            curr_path_dict[curr_node] = count
            curr_path.append((curr_node,count))
            if count > max_dist:
                max_dist = count
            count += 1
            curr_node = l[curr_node] - 1

        if curr_node in curr_path_dict:
            distance_dict[curr_node] = count - curr_path_dict[curr_node]
            for i in range(curr_path_dict[curr_node]):
                distance_dict[curr_path[i][0]] = count + (curr_path_dict[curr_node] - curr_path[i][1])

    return max_dist


# print(longest_path([4, 1, 2, 1]))
# print(longest_path([4, 3, 5, 1, 2]))
# print(longest_path([2, 4, 2, 2, 3]))
#
print(longest_path2([4, 1, 2, 1]))
print(longest_path2([4, 3, 5, 1, 2]))
print(longest_path2([2, 4, 2, 2, 3]))
#
# print("*****************")
# print(getMaxVisitableWebpages(4, [4, 1, 2, 1]))
# print(getMaxVisitableWebpages(5, [4, 3, 5, 1, 2]))
# print(getMaxVisitableWebpages(5, [2, 4, 2, 2, 3]))

# temp= [i+1 for i in range(499)]
# temp.append(500)
# print(temp)

#zprint(getMaxVisitableWebpages(len(temp), temp)