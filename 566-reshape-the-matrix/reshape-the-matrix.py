class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != r * c:
            return mat

        arr = []

        for i in range(rows):
            for j in range(cols):
                arr.append(mat[i][j])

        ans = []
        index = 0

        for i in range(r):
            row = []

            for j in range(c):
                row.append(arr[index])
                index += 1

            ans.append(row)

        return ans