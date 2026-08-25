class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        arr = [[-1] * n] * m 

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 or c == n-1:
                    arr[r][c] = 1 # one unique path to trophy
                else:
                    arr[r][c] = arr[r+1][c] + arr[r][c+1]

        return arr[0][0]