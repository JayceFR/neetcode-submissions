class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        def dp(s):
            if s == "":
                return True
            if s in memo:
                return memo[s]
            for word in wordDict:
                if s.startswith(word):
                    if dp(s[len(word):]):
                        return True 
            memo[s] = False 
            return False 
        
        return dp(s)
