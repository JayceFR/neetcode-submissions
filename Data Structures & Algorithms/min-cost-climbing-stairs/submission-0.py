class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dp(pos):
            if pos >= len(cost):
                # completed climbing the stairs
                return 0 
            
            return cost[pos] + min(dp(pos+1), dp(pos+2))
        
        return min(dp(0), dp(1))