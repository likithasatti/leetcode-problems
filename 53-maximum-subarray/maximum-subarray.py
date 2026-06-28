class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=nums[0]
        maxi=nums[0]
        for i in nums[1:]:
            current=max(i,current+i)
            maxi=max(maxi,current)
        return maxi    