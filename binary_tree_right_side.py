from __future__ import annotations


# time complexity: O(log(n))
# space complexity: O(log(n))
def get_right_side_list(l: list[int | None]) -> list[int | None]:
    """return the right side of a tree, assuming list represents a tree in top-bottom-left-to-right order"""
    output = []
    i = 0

    while i < len(l):
        output.append(l[i])
        i = 2*i + 2

    return output


print(get_right_side_list([1, 2, 3, None, 5, None, 4]))
print(get_right_side_list([1, None, 3]))

