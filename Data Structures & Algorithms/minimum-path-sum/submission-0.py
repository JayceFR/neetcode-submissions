class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp, can do it space optimised to extra O(1)
        
        ROWS, COLS = len(grid), len(grid[0])

        # handle the boundaries 
        for x in range(ROWS - 2, -1, -1):
            grid[x][COLS-1] += grid[x+1][COLS-1]
        for y in range(COLS - 2, -1, -1):
            grid[ROWS-1][y] += grid[ROWS-1][y+1]

        for x in range(ROWS-2, -1, -1):
            for y in range(COLS - 2, -1, -1):
                grid[x][y] += min(grid[x+1][y], grid[x][y+1])
        
        return grid[0][0]
                
