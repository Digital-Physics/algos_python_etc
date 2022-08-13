# time complexity: O(n)
# space complexity: O(1)


def min_comp_count(s: list[int]) -> int:
    """get the minimum number of competitions (worth either 1 or 2) based on scoreboard totals inference"""
    largest_even = 0
    largest_odd = 0
    min_comps_needed_even = 0
    min_comps_needed_odd = 0

    for num in s:
        if num % 2 == 0 and num > largest_even:
            min_comps_needed_even = int(num / 2)
            largest_even = num
        elif num % 2 == 1 and num > largest_odd:
            min_comps_needed_odd = int(num // 2 + 1)
            largest_odd = num

    if largest_even > largest_odd:
        if largest_odd != 0:
            return min_comps_needed_even + 1
        else:
            return min_comps_needed_even
    else:
        return min_comps_needed_odd


print(min_comp_count([1, 2, 3, 4, 5, 6]))
print(min_comp_count([4, 3, 3, 4]))
print(min_comp_count([2, 4, 6, 8]))




