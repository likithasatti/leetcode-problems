class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for k in range(4):

            if mat == target:
                return True

            n = len(mat)

            new = []

            for j in range(n):
                row = []

                for i in range(n - 1, -1, -1):
                    row.append(mat[i][j])

                new.append(row)

            mat = new

        return False