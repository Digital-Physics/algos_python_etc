# time complexity: O(n)
# space complexity: O(1)
def max_product(l: list[int]) -> int:
    max_prod = float("-inf")
    pos_preceding_product = None
    neg_preceding_product = None

    for num in l:
        """return the product of the contiguous subarray with the largest product"""
        if num < 0:
            if neg_preceding_product:
                pos_preceding_product = neg_preceding_product * num
                neg_preceding_product = None
            elif pos_preceding_product:
                neg_preceding_product = pos_preceding_product * num
                pos_preceding_product = None
            else:
                neg_preceding_product = num
        elif num > 0:
            if neg_preceding_product:
                neg_preceding_product = neg_preceding_product * num
                pos_preceding_product = None
            elif pos_preceding_product:
                pos_preceding_product = pos_preceding_product * num
                neg_preceding_product = None
            else:
                pos_preceding_product = num
        else:  # == 0
            pos_preceding_product = None
            neg_preceding_product = None

        # update max
        if pos_preceding_product:
            if pos_preceding_product > max_prod:
                max_prod = pos_preceding_product
        elif neg_preceding_product:
            if neg_preceding_product > max_prod:
                max_prod = neg_preceding_product
        else:
            if 0 > max_prod:
                max_prod = 0

    return max_prod


print(max_product([2, 3, -2, 4]))
print(max_product([2, 3, -2, 4, -3]))
print(max_product([-2, 0, -1]))
print(max_product([-1]))


