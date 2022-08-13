# time complexity: O(n)
# space complexity: O(1)
def frogs_jumping(n: int, p: list[int]) -> int:
    """find the min number of jumps for frogs to clear an n-lily pad vector. frogs (idx p) jump to next open cell/pad."""
    min_idx = float("inf")
    max_idx = float("-inf")

    f = len(p)

    for i in range(len(p)):
        if p[i] < min_idx:
            min_idx = p[i]
        if p[i] > max_idx:
            max_idx = p[i]

    # empty spaces between last and first frog
    empty_spaces = (max_idx - min_idx - 1) - (f - 2)
    gap_to_end = n - max_idx - 1

    return empty_spaces + gap_to_end + f


print(frogs_jumping(3, [1]))
print(frogs_jumping(6, [5, 2, 4]))
