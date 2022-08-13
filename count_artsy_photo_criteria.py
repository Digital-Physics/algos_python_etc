# # time: O(N*(Y-X)**2)
# # space: O(N) for making the reversed list (could be optimized by doing just one pass)
# def one_way(n_s: int, c_s: str, x_s: int, y_s: int) -> int:
#     count = 0
#
#     for p_idx in range(n_s):
#         if c_s[p_idx] == "P":
#             for a_idx in range(p_idx + x_s, p_idx + y_s + 1):
#                 if a_idx < n_s and c_s[a_idx] == "A":
#                     for b_idx in range(a_idx + x_s, a_idx + y_s + 1):
#                         if b_idx < n_s and c_s[b_idx] == "B":
#                             count += 1
#
#     return count
#
#
# # a photo is artsy if both the distance between the photographer P and artist A is within X and Y
# # the distance between the photographer P and background B is in range
# def count_artsy_photo(n: int, c: str, x: int, y: int) -> int:
#     reverse = c[::-1]
#     return one_way(n, c, x, y) + one_way(n, reverse, x, y)
#
#
# # time: O(N*(Y-X)**2)
# # space: O(1)
# def count_artsy_photo2(n: int, c: str, x: int, y: int) -> int:
#     count = 0
#
#     for p_idx in range(n):
#         if c[p_idx] == "P":
#             for a_idx in range(p_idx + x, p_idx + y + 1):
#                 if a_idx < n and c[a_idx] == "A":
#                     for b_idx in range(a_idx + x, a_idx + y + 1):
#                         if b_idx < n and c[b_idx] == "B":
#                             count += 1
#
#     for b_idx in range(n):
#         if c[b_idx] == "B":
#             for a_idx in range(b_idx + x, b_idx + y + 1):
#                 if a_idx < n and c[a_idx] == "A":
#                     for p_idx in range(a_idx + x, a_idx + y + 1):
#                         if p_idx < n and c[p_idx] == "P":
#                             count += 1
#
#     return count
#
# # time: O()
# def count_artsy_photo3(C: str, X: int, Y: int) -> int:
#     count = 0
#     l_idx = 0
#     r_idx = len(C) - 1
#
#     while l_idx < r_idx:
#         if C[l_idx] == "P":
#             first = True
#             for i in range(r_idx, l_idx, -1):
#                 if C[i] == "B":
#                     if first:
#                         r_idx = i
#                         first = False
#                     mid_range_high = min(l_idx + Y, i - X)
#                     mid_range_low = max(l_idx + X, i - Y)
#                     count += sum((1 if C[a] == "A" else 0 for a in range(mid_range_low, mid_range_high + 1)))
#             l_idx += 1
#         elif C[l_idx] == "B":
#             first = True
#             for i in range(r_idx, l_idx, -1):
#                 if C[i] == "P":
#                     if first:
#                         r_idx = i
#                         first = False
#                     mid_range_high = min(l_idx + Y, i - X)
#                     mid_range_low = max(l_idx + X, i - Y)
#                     count += sum((1 if C[a] == "A" else 0 for a in range(mid_range_low, mid_range_high + 1)))
#             l_idx += 1
#         else:
#             l_idx += 1
#
#     return count
#
#
# def count_artsy_photo4(C: str, X: int, Y: int) -> int:
#     print("start", C)
#     l_idx = 0
#     r_idx = len(C) - 1
#
#     window_l, window_r = overlap_window(l_idx, r_idx, X, Y)
#     print("initial left and right of window", window_l, window_r)
#
#     if window_l is not None:
#         a_s = sum((1 if C[a] == "A" else 0 for a in range(window_l, window_r + 1)))
#     else:
#         a_s = 0
#
#     # print("Initial A's in window:", a_s)
#     print('get pab')
#     pab_total = one_way_count(C, X, Y, "P", a_s)
#     print('get bap')
#     bap_total = one_way_count(C, X, Y, "B", a_s)
#     print("total pab, bap", pab_total, bap_total)
#     return pab_total + bap_total
#
#
# def one_way_count(C: str, X: int, Y: int, target: chr, a_count: int) -> int:
#     total = 0
#     l_idx = 0
#     r_idx = len(C) - 1
#     if target == "P":
#         last_letter = "B"
#     else:
#         last_letter = "P"
#
#     while l_idx + X < len(C):
#         print(target, "and l idx is", l_idx)
#         if C[l_idx] == target:
#             # a_count = a_count_update(C, X, Y, a_count, l_idx, r_idx, -1)
#             print("found target", target, "at", l_idx)
#             # print("look for last letter", last_letter)
#             for r_idx in range(len(C)-1, l_idx + X, -1):
#                 if C[r_idx] == last_letter:
#                     print("last letter match at", r_idx)
#                     print("total += previous round a_count", a_count)
#                     total += a_count
#                 print("r_idx countdown idx dif for next round after", r_idx)
#                 print("a_count b4", a_count)
#                 a_count = a_count_update(C, X, Y, a_count, l_idx, r_idx, -1)
#                 print("a_count after (for next round)", a_count)
#
#             a_count = a_count_update(C, X, Y, a_count, l_idx, r_idx, 1)
#             l_idx += 1
#         else:
#             a_count = a_count_update(C, X, Y, a_count, l_idx, r_idx, 1)
#             l_idx += 1
#
#         # r_idx = len(C) - 1 # reset
#
#     return total
#
#
# def a_count_update(C: str, X: int, Y: int, a_count: int, l_idx: int, r_idx: int, delta: int):
#     # print("calc before:")
#     window_l, window_r = overlap_window(l_idx, r_idx, X, Y)
#
#     # print("calc after:")
#     if delta == 1:
#         window_l_after, window_r_after = overlap_window(l_idx + 1, r_idx, X, Y)
#     elif delta == -1:
#         window_l_after, window_r_after = overlap_window(l_idx, r_idx - 1, X, Y)
#
#     if window_l_after is None:
#         # print("no window after")
#         return 0
#     elif window_l is None:
#         # print("new window, so how many As?")
#         return sum((1 if C[i] == "A" else 0 for i in {window_l_after, window_r_after}))
#     else:
#         a_before = sum((1 if C[i] == "A" else 0 for i in {window_l, window_r}))
#         a_after = sum((1 if C[i] == "A" else 0 for i in {window_l_after, window_r_after}))
#
#         return a_count + (a_after - a_before)
#
#
# def overlap_window(l_idx: int, r_idx: int, X: int, Y: int):
#     l_lower = l_idx + X
#     l_upper = l_idx + Y
#     r_lower = r_idx - Y
#     r_upper = r_idx - X
#     print("overlap window components", l_lower, l_upper, r_lower, r_upper)
#
#     if l_upper < r_lower or l_lower > r_upper:  # second clause shouldn't happen
#         return None, None
#     else:
#         window_l = max(l_lower, r_lower)
#         window_r = min(l_upper, r_upper)
#         print("window calced", window_l, window_r)
#
#         return window_l, window_r
# print(count_artsy_photo(5, test_cases[0], 1, 2))
# print(count_artsy_photo(5, test_cases[1], 2, 3))
# print(count_artsy_photo(8, test_cases[2], 1, 3))
# print(count_artsy_photo(8, test_cases[3], 1, 3))
# print()
# print(count_artsy_photo2(5, test_cases[0], 1, 2))
# print(count_artsy_photo2(5, test_cases[1], 2, 3))
# print(count_artsy_photo2(8, test_cases[2], 1, 3))
# print(count_artsy_photo2(8, test_cases[3], 1, 3))
# print()
# print(count_artsy_photo3(test_cases[0], 1, 2))
# print(count_artsy_photo3(test_cases[1], 2, 3))
# print(count_artsy_photo3(test_cases[2], 1, 3))
# print(count_artsy_photo3(test_cases[3], 1, 3))
from collections import deque


# time complexity: O(n*max(Y-X, X))
# def count_artsy_photo(C: str, X: int, Y: int) -> int:
#     states = []
#     total = 0
#
#     p_waiting_for_a = deque([])
#     states.append(p_waiting_for_a)
#     b_waiting_for_a = deque([])
#     states.append(b_waiting_for_a)
#     p_looking_for_a = deque([])
#     states.append(p_looking_for_a)
#     b_looking_for_a = deque([])
#     states.append(b_looking_for_a)
#     pa_looking_for_b = deque([])
#     states.append(pa_looking_for_b)
#     ba_looking_for_p = deque([])
#     states.append(ba_looking_for_p)
#
#     # change states & count
#     for num in range(len(C)):
#         print("letter", C[num])
#
#         # remove & move items based on thresholds
#         while p_waiting_for_a and p_waiting_for_a[0] >= X:
#             p_waiting_for_a.popleft()
#             p_looking_for_a.append(0)
#         # for i in range(len(p_waiting_for_a)):
#         #     if p_waiting_for_a[i] >= X:
#         #         p_looking_for_a.append(1)
#         #     else:
#         #         break
#
#         # while b_waiting_for_a and b_waiting_for_a[0] > Y:
#         while b_waiting_for_a and b_waiting_for_a[0] >= X:
#             b_waiting_for_a.popleft()
#             b_looking_for_a.append(0)
#         # for i in range(len(b_waiting_for_a)):
#         #     if b_waiting_for_a[i] >= X:
#         #         b_looking_for_a.append(1)
#         #     else:
#         #         break
#
#         while p_looking_for_a and p_looking_for_a[0] > Y - X:
#             p_looking_for_a.popleft()
#
#         while b_looking_for_a and b_looking_for_a[0] > Y - X:
#             b_looking_for_a.popleft()
#
#         while pa_looking_for_b and pa_looking_for_b[0] > Y:
#             pa_looking_for_b.popleft()
#
#         while ba_looking_for_p and ba_looking_for_p[0] > Y:
#             ba_looking_for_p.popleft()
#
#         print("before adding letter", states)
#         # add new num associated w/ letter to list and count any "bap" and "pab"; put in new states based on letter
#         if C[num] == "P":
#             p_waiting_for_a.append(0)
#             # if X == 1:
#             #     p_looking_for_a.append(0)
#             for m in range(len(ba_looking_for_p)):
#                 total += 1 if ba_looking_for_p[m] >= X else 0
#                 print('total', total)
#         elif C[num] == "B":
#             b_waiting_for_a.append(0)
#             # if X == 1:
#             #     b_looking_for_a.append(0)
#             for n in range(len(pa_looking_for_b)):
#                 total += 1 if pa_looking_for_b[n] >= X else 0
#                 print('total', total)
#         elif C[num] == "A":
#             for j in range(len(b_looking_for_a)):
#                 if b_looking_for_a[j] >= X:
#                     ba_looking_for_p.append(0)
#             for k in range(len(p_looking_for_a)):
#                 if p_looking_for_a[k] >= X:
#                     print("one pa", p_looking_for_a[k])
#                     pa_looking_for_b.append(0)
#
#         # update counts in states
#         for state in states:
#             for l in range(len(state)):
#                 state[l] += 1
#
#         print(states)
#
#     return total
#
#
# test_cases = ["APABA", "APABA", ".PBAAP.B", "APBPBAA.PAB"]
#
# # print(count_artsy_photo(test_cases[0], 1, 2))
# # print(count_artsy_photo(test_cases[1], 2, 3))
# print(count_artsy_photo(test_cases[2], 1, 3))
# # print(count_artsy_photo(test_cases[3], 1, 3))
#

# time complexity: O(n*max(Y-X, X))
def count_artsy_photo(C: str, X: int, Y: int) -> int:
    states = []
    total = 0

    p_looking_for_a = deque([])
    states.append(p_looking_for_a)
    b_looking_for_a = deque([])
    states.append(b_looking_for_a)
    pa_looking_for_b = deque([])
    states.append(pa_looking_for_b)
    ba_looking_for_p = deque([])
    states.append(ba_looking_for_p)

    # change states & count
    for num in range(len(C)):
        while p_looking_for_a and p_looking_for_a[0] > Y:
            p_looking_for_a.popleft()

        while b_looking_for_a and b_looking_for_a[0] > Y:
            b_looking_for_a.popleft()

        while pa_looking_for_b and pa_looking_for_b[0] > Y:
            pa_looking_for_b.popleft()

        while ba_looking_for_p and ba_looking_for_p[0] > Y:
            ba_looking_for_p.popleft()

        print("before adding letter", states)
        # add new num associated w/ letter to list and count any "bap" and "pab"; put in new states based on letter
        if C[num] == "P":
            p_looking_for_a.append(0)
            # if X == 1:
            #     p_looking_for_a.append(0)
            for m in range(len(ba_looking_for_p)):
                total += 1 if ba_looking_for_p[m] >= X else 0
                print('total', total)
        elif C[num] == "B":
            b_looking_for_a.append(0)
            # if X == 1:
            #     b_looking_for_a.append(0)
            for n in range(len(pa_looking_for_b)):
                total += 1 if pa_looking_for_b[n] >= X else 0
                print('total', total)
        elif C[num] == "A":
            for j in range(len(b_looking_for_a)):
                if b_looking_for_a[j] >= X:
                    ba_looking_for_p.append(0)
            for k in range(len(p_looking_for_a)):
                if p_looking_for_a[k] >= X:
                    print("one pa", p_looking_for_a[k])
                    pa_looking_for_b.append(0)

        # update counts in states
        for state in states:
            for l in range(len(state)):
                state[l] += 1

        print(states)

    return total


test_cases = ["APABA", "APABA", ".PBAAP.B", "APBPBAA.PAB"]

print(count_artsy_photo(test_cases[0], 1, 2))
print(count_artsy_photo(test_cases[1], 2, 3))
print(count_artsy_photo(test_cases[2], 1, 3))
# print(count_artsy_photo(test_cases[3], 1, 3))






