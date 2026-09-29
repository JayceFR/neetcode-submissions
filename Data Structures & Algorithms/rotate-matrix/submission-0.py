class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # same as reversing the rows and then transposing the matrix 
        matrix.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        