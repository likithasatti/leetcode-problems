class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alti=0
        maxi=0
        for i in gain:
            alti+=i
            if alti>maxi:
                maxi=alti
        return maxi        

        