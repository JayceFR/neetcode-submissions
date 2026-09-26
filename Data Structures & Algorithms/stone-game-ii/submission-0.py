class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # state is alic, M, i 
        dp = {}
        def dfs(M, i, alice = True):
            if i >= len(piles):
                return 0 
            if (alice, i, M) in dp:
                return dp[(alice, i, M)]
            res = 0 if alice else float("inf")
            total = 0 
            for x in range(1, (2 * M) + 1):
                if i + x > len(piles):
                    break 
                # We take X balls from i 
                total += piles[i + x - 1]
                if alice:
                    res = max(res, total + dfs(max(M, x), i + x, not alice))
                else:
                    res = min(res, dfs(max(M, x), i + x, not alice))
            dp[(alice, i, M)] = res 
            return res 
        
        return int(dfs(1, 0, True))

