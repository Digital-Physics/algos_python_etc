# time complexity: O(n)
# space complexity: O(1)


def count_deflates(r: list[int]) -> int:
    """count how many tubes in a stack you have to deflate to make a stack stable (strictly int decreasing)"""
    last_tube = r.pop()
    deflate_count = 0

    while r:
        tube = r.pop()
        if tube >= last_tube:
            tube = last_tube - 1  # deflate
            if tube <= len(r):
                return -1
            deflate_count += 1
        last_tube = tube

    if last_tube >= 1:
        return deflate_count
    else:
        return -1


print(count_deflates([2, 5, 3, 6, 5]))
print(count_deflates([100, 100, 100]))
print(count_deflates([6, 5, 4, 3]))

