class Permute:
    def __init__(self, nums: list[int]) -> None:
        self.output = []
        self.nums = nums

    def permute_helper(self, nums: list[int], partial: list[int] = []) -> list[list[int]]:
        """generate permutations of a list"""
        if not nums:
            self.output.append(partial)
        else:
            for i, num in enumerate(nums):
                leftover_nums = nums[:i] + nums[i+1:] if i + 1 < len(nums) else nums[:i]
                self.permute_helper(leftover_nums, partial + [num])

        return permute.output


permute = Permute([1, 2, 3])
print(permute.permute_helper(permute.nums))



