from __future__ import annotations


def max_water_area(wall_heights: list[int]) -> int:
    """Returns the max area of a pool where the height is the min of two sides."""
    l_idx = 0
    r_idx = len(wall_heights) - 1
    max_area = 0

    while l_idx < r_idx:
        if wall_heights[l_idx] <= wall_heights[r_idx]:
            max_area = max(max_area, wall_heights[l_idx]*(r_idx - l_idx))
            # We can increment the lower value's index because it will never be needed again.
            # If it was paired w/ another ending wall it would have less width and the height would be the same or worse(since it was lower)
            l_idx += 1
        else:
            max_area = max(max_area, wall_heights[r_idx]*(r_idx - l_idx))
            # We can increment the upper value's index because it will never be needed again.
            # If it was paired w/ another start wall, it would have less width and the height would be the same or worse(since it was lower)
            r_idx -= 1

    return max_area


print(max_water_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))