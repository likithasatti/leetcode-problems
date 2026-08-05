class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        col=len(matrix[0])
        ans=[]
        for j in range(col):
            row=[]
            for i in range(rows):
                row.append(matrix[i][j]) 
            ans.append(row)
        return ans   