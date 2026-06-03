class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result=[]
        for i in nums:
            if i!=0:
                result.append(i)
        while len(result)<len(nums):
            result.append(0)
        nums[:]=result           

