class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r, c = len(matrix), len(matrix[0])
        self.prefix = [[0] * (c+1) for _ in range(r+1)]
        for cr in range(r):
            acc = 0
            for cc in range(c):
                acc += matrix[cr][cc] 
                self.prefix[cr+1][cc+1] = self.prefix[cr][cc+1] + acc 
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.prefix[row2][col2]
        above = self.prefix[row1 - 1][col2]
        left = self.prefix[row2][col1 - 1]
        topLeft = self.prefix[row1 - 1][col1 - 1]
        return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)