# time: O(c)
# space: O(1)

# given a spinny lock that starts at 1 and goes to n, find the shortest time if it takes 1 sec/unit twist
def shortest_lock_twist(n: int, c: list[int]) -> int:
    total = 0
    wheel = 1

    for num in c:
        if num != wheel:
            total += min(abs(num - wheel), n - abs(num - wheel))
            wheel = num

    return total


print(shortest_lock_twist(10, [9, 4, 4, 8]))
