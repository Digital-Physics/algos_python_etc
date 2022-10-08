from __future__ import annotations
# https://leetcode.com/problems/range-sum-query-mutable/discuss/1280869/Python%3A-All-possible-methods-Explained-with-time-and-space-complexity.


class NumArray:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left: right+1])


test_list = [1, 7, 11, 23]

num_obj = NumArray(test_list)
num_obj.update(0, 20)
print(num_obj.sumRange(0, 1))


class NumArray2:
    """this version is good if there are lots of numbers to sum in the middle and the right side is long.
    we can do sumRange() in constant instead of linear time in the size of the middle piece, but update() is now linear..."""
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums
        self.prefix_sums = [0]
        for i in range(len(self.nums)):
            self.prefix_sums[i] = self.prefix_sums[-1] + self.nums[i]

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        diff = val - self.nums[index]

        for i in range(index + 1, len(self.nums)):
            self.prefix_sums[i] += diff

    def sumRange(self, left: int, right: int) -> int:
        """the prefix_sum was initialized with an extra value, 0, at the start of the list.
        convince yourself we don't need the left+1 index by doing a simple example"""
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


num_obj2 = NumArray(test_list)
num_obj2.update(0, 20)
print(num_obj2.sumRange(0, 1))


class NumArray3:
    """left to the reader :)... this version is good if you like trees and sub-linear (log) time updates"""
    def __init__(self, nums: list[int]) -> None:
        pass

    def update(self, index: int, val: int) -> None:
        pass

    def sumRange(self, left: int, right: int) -> int:
        pass
