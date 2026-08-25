class Solution:
    def numDecodings(self, s: str) -> int:
        
        if len(s) == 0:
            return 0 
        
        memo = [-1 for x in range(len(s))]

        def dp(pos):
            if pos >= len(s):
                # reached the end of a valid path 
                return 1 
            
            if memo[pos] != -1:
                return memo[pos]
            
            if s[pos] == "0":
                return 0 # can't do anything with 0 
            
            if s[pos] == "1":
                if pos + 1 < len(s) and int(s[pos+1]) <= 9:
                    memo[pos] = dp(pos+1) + dp(pos+2)
                    return memo[pos]
            
            if s[pos] == "2":
                if pos + 1 < len(s) and int(s[pos+1]) <= 6:
                    memo[pos] = dp(pos+1) + dp(pos+2)
                    return memo[pos]
            
            memo[pos] = dp(pos+1)
            return memo[pos]
        
        return dp(0)
            

