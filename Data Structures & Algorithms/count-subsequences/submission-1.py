class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # state as (i, j) where i is the pos in s and j is the pos in t 
        # dfs(i,j) returns the number of distinct ways of generating subsequences 
        #                  from i at s to get from j at t 

        '''
        i 0 1 2 3 j  
        0       1
        1       1
        2       1
        3       1
        4       1
        5 0 0 0 0

        s = caaat
        t = cat

        dp[i][j] = dp[i+1][j+1] + dp[i+1][j] if s[i] == s[j] else dp[i+1][j]
        '''
        # Top down sol: Time complexity: O(m * n) as the states are (i, j)
        # memo = {}
        # def dfs(i,j):
        #     # base case 
        #     if j >= len(t):
        #         return 1 
        #     if i >= len(s):
        #         return 0 
        #     if (i,j) in memo:
        #         return memo[(i,j)]
            
        #     res = 0 

        #     if s[i] == t[j]:
        #         # there is one match, we can increment j or ignore it as well 
        #         res += dfs(i+1, j+1)
        #     res += dfs(i+1, j)

        #     memo[(i,j)] = res 
        #     return res 

        # return dfs(0,0)

        # Bottom up sol: Space optimised 
        I, J = len(s), len(t)
        dp = [0] * (J + 1)
        dp[-1] = 1 

        for i in range(I-1, -1, -1):
            new_dp = [0] * (J+1)
            new_dp[-1] = 1 
            
            for j in range(J-1, -1, -1):
                new_dp[j] = dp[j+1] + dp[j] if s[i] == t[j] else dp[j]

            dp = new_dp

        return dp[0]
