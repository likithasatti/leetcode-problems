class Solution:
    def maxFrequencyElements(self, nums):

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        maximum = max(freq.values())

        count = 0

        for value in freq.values():
            if value == maximum:
                count += value

        return count