class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
         data = [0] * 101  

         for i in nums:
            data[i] += 1  
            if data[i] > 2: return False  

         return True