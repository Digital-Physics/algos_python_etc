# time complexity: O(n)
# space complexity: O(1)
def find_dup(l: list[int]) -> int:
    """find dup in list of length n + 1 of integers 1 to n.
    Use only a constant amount of auxiliary space,
    and don't modify the input."""
    expected_sum = (len(l)-1)*(len(l) - 1 + 1)//2
    return sum(l) - expected_sum


print(find_dup([1, 3, 4, 2, 2]))
print(find_dup([3, 1, 3, 4, 2]))
print(find_dup([3, 1, 2, 4, 1]))
print(find_dup([1, 2, 3, 6, 4, 5, 5]))
