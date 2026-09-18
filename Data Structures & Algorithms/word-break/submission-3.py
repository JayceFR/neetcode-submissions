class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Top down solution 

        memo = {}
        def dp(pos) -> bool:
            if pos >= len(s):
                return True 
            if pos in memo:
                return memo[pos]

            for word in wordDict:
                if s[pos:].startswith(word):
                    if dp(pos+len(word)):
                        memo[pos] = True 
                        return memo[pos]
            memo[pos] = False 
            return memo[pos]

        return dp(0)    
