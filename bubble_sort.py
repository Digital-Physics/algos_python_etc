# time complexity: O(n**2) where n is the length of the input array
# we do passes of length n-1, n-2, ... 0 in the worse case scenario
# this means (n-1)*n/2 steps, which is O(n**2)
#
# space complexity: O(1), constant space
# we only use a finite number of variables (2) that won't grow as the length of the array increases
def bubble_sort(array):
    swapped_last_round = True
    # we will be looking one idx ahead so we don't want to go out of bounds on array
    end_idx = len(array)-1

    while swapped_last_round:
        swapped_last_round = False
        for i in range(end_idx):
            if array[i] > array[i+1]:
                swap_elements_in_place(array, i, i+1)
                swapped_last_round = True
        end_idx -= 1

    return array


# note: we don't return anything from this helper function
# is this even helpful since the function is only one line? probably not, but helper functions are usually nice to employ.
# you could have swapped the array elements one at a time (the long way), in which case the helper function is nice:
    # temp = array[idx_1] # temp variable points to same object as
    # array[idx_1] = array[idx_2] # array[ind_1] is reassigned and now points to new immutable Int object (same one array[idx_2] points to)
    # array[idx_2] = temp # array[int_2] is bound to new object, the one temp points to, which is still the original immutable int object
def swap_elements_in_place(array, idx_1, idx_2):
    array[idx_1], array[idx_2] = array[idx_2], array[idx_1]
    

print(bubble_sort([]))
print(bubble_sort([2, 7, 1, -4]))
