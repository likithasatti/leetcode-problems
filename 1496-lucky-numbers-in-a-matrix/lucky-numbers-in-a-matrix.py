class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):

            minimum = min(matrix[i])
            col = matrix[i].index(minimum)

            largest = True

            for j in range(rows):

                if matrix[j][col] > minimum:
                    largest = False

            if largest:
                ans.append(minimum)

        return ans