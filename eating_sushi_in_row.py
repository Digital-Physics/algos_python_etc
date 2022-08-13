from collections import deque
# count how many items in d you will eat. you eat any item you haven't eaten in the past k items.


# time: O(d)
# space: O(k)
def count_eaten(d: list[int], k: int) -> int:
    eaten = {}
    lru_queue = deque([])
    count = 0

    for int_item in d:
        if int_item not in eaten:
            eaten[int_item] = True
            count += 1

            lru_queue.append(int_item)
            if len(lru_queue) > k:
                item_to_drop = lru_queue.popleft()
                del eaten[item_to_drop]

    return count


print(count_eaten([1, 2, 3, 3, 2, 1], 2))
