class Solution:
    def secondHighest(self, s: str) -> int:

        nums = []

        for ch in s:
            if ch.isdigit():
                nums.append(int(ch))

        nums = list(set(nums))

        if len(nums) < 2:
            return -1

        nums.sort()

        return nums[-2]