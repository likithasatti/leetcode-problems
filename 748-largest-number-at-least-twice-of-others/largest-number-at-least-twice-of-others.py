class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        maximum = max(nums)
        index = nums.index(maximum)

        for num in nums:
            if num != maximum and maximum < 2 * num:
                return -1

        return index