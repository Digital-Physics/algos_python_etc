# merge sort divides the array in half, sorts left and right sides, and merges the sorted lists back together
# usually it is implemented recursively, but we're going to try it iteratively here
# time: O(n*log(n)) (best/avg/worst)
# space: O(n)? Does this take less space then recursive approach that passes arrays (not idx) in merge f?
def merge_sort(array):
    list_of_sorted_lists = []

    for i in range(len(array)):  # (linear time, linear space followed by...)
        # initialize for function by putting each element in a list of its own
        list_of_sorted_lists.append([array[i]])

    while len(list_of_sorted_lists) > 1:  # (outer while loop is log time complexity)
        temp = []
        list_idx = 0

        # (this while loop is linear in the size of number lists, and the number of individual elements)
        # (we only touch each base element in the merge process once, so overall linear even though it is nested)
        while list_idx < len(list_of_sorted_lists):
            if list_idx + 1 == len(list_of_sorted_lists):
                temp.append(list_of_sorted_lists[list_idx])
                list_idx += 1
            else:  # (merge sort is linear in the size of the two sorted lists)
                temp.append(merge_sorted_lists(list_of_sorted_lists[list_idx], list_of_sorted_lists[list_idx+1]))
                list_idx += 2

        list_of_sorted_lists = temp

    if len(list_of_sorted_lists) > 0:
        return list_of_sorted_lists[0]
    else:
        return []


def merge_sorted_lists(l_arr, r_arr):
    sorted_out = [None for _ in range(len(l_arr) + len(r_arr))]

    curr_idx_l = 0
    curr_idx_r = 0
    sorted_idx = 0

    while curr_idx_l < len(l_arr) and curr_idx_r < len(r_arr):
        if l_arr[curr_idx_l] <= r_arr[curr_idx_r]:
            sorted_out[sorted_idx] = l_arr[curr_idx_l]
            curr_idx_l += 1
            sorted_idx += 1
        else:
            sorted_out[sorted_idx] = r_arr[curr_idx_r]
            curr_idx_r += 1
            sorted_idx += 1

    while curr_idx_l < len(l_arr):
        sorted_out[sorted_idx] = l_arr[curr_idx_l]
        curr_idx_l += 1
        sorted_idx += 1

    while curr_idx_r < len(r_arr):
        sorted_out[sorted_idx] = r_arr[curr_idx_r]
        curr_idx_r += 1
        sorted_idx += 1

    return sorted_out


print(merge_sort([]))
print(merge_sort([2, 7, 1, -4]))
