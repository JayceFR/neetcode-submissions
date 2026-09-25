class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # edge case, if the end itself is an obstacle: Cooked 
        if obstacleGrid[-1][-1] == 1:
            return 0 
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * (COLS + 1)
        # base case 
        dp[COLS - 1] = 1 
        for x in range(ROWS-1, -1, -1):
            new_dp = [0] * (COLS + 1)
            for y in range(COLS-1, -1, -1):
                if obstacleGrid[x][y] == 1:
                    new_dp[y] = 0 
                else:
                    new_dp[y] = dp[y] + new_dp[y+1]
            dp = new_dp
        
        return dp[0]

