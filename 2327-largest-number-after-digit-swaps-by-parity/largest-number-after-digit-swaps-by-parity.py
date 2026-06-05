class Solution:
    def largestInteger(self, num: int) -> int:

        odd = sorted([int(d) for d in str(num) if int(d) % 2], reverse=True)
        even = sorted([int(d) for d in str(num) if int(d) % 2 == 0], reverse=True)

        result = ""

        for d in str(num):
            if int(d) % 2:
                result += str(odd.pop(0))
            else:
                result += str(even.pop(0))

        return int(result)