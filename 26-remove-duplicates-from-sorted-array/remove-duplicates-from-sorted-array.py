class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique = []

        for num in nums:
            if num not in unique:
                unique.append(num)

        nums[:len(unique)] = unique

        return len(unique)