class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # state as (i, j) where i is the pos in s and j is the pos in t 
        # dfs(i,j) returns the number of distinct ways of generating subsequences 
        #                  from i at s to get from j at t 
        memo = {}
        def dfs(i,j):
            # base case 
            if j >= len(t):
                return 1 
            if i >= len(s):
                return 0 
            if (i,j) in memo:
                return memo[(i,j)]
            
            res = 0 

            if s[i] == t[j]:
                # there is one match, we can increment j or ignore it as well 
                res += dfs(i+1, j+1)
            res += dfs(i+1, j)

            memo[(i,j)] = res 
            return res 

        return dfs(0,0)