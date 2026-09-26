class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Didn't get this question at the start 
        # But we would basically need to form a target 
        # Which is just a knapsack problem. 
        # I am going to do it with a 2 dp bottom up. 

        # We can space optimise it as well. 
        total = sum(stones)
        target = total // 2 
        
        dp = [False] * (target + 1)
        dp[0] = True 

        for i in range(len(stones)):
            new_dp = [False] * (target + 1)
            new_dp[0] = True 
            for y in range(1, target + 1):
                new_dp[y] = dp[y] or dp[y - stones[i]] if stones[i] <= y else dp[y]
            dp = new_dp
        print(dp)
        # Now get the max one
        for y in range(target, -1, -1):
            if dp[y]:
                return abs(y - (total - y))

        return 0 
