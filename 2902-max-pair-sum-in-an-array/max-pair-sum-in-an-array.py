class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def maxDigit(num):
            largest=0
            while num>0:
                digit=num%10
                if digit>largest:
                    largest=digit
                num=num//10
            return largest   
        ans = -1

        n = len(nums)

        for i in range(n):

            for j in range(i + 1, n):

                if maxDigit(nums[i]) == maxDigit(nums[j]):

                    ans = max(ans, nums[i] + nums[j])

        return ans     
