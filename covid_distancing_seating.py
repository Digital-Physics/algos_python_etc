# time complexity: s*log(s) + s = O(s*log(s))
# space: O(1) since we sort in place and don't use any auxiliary memory besides a few constants
# or is space O(n) since when we append just one element to s and extend the array, we double the size?
# so we don't get to take advantage of amortizing the space over many appends?

# n is seats at bench, k is distance between seats, m = len(s), filled seat indices ->
# return count of additional diners that can be added in between people already seated
def additional_diners(n: int, k: int, m: int, s: list[int]) -> int:
    s.sort()
    s.append(n + 1)  # we want our for loop to look at the gap after the last seated diner

    start_idx = 0
    chunk_size = k + 1  # person and one distance gap to either the left or right
    total_added = 0

    for i, person_idx in enumerate(s):
        if start_idx == 0 or i == m:  # first or last slot
            dist = person_idx - start_idx - 1  # -1 for index diff
        else:  # middle slot
            dist = person_idx - start_idx - 1 - k  # -1 for index diff, - K for initial space needed

        start_idx = person_idx

        total_added += dist // chunk_size

    return total_added


print(additional_diners(10, 1, 2, [2, 6]))
print(additional_diners(15, 2, 3, [11, 6, 14]))

