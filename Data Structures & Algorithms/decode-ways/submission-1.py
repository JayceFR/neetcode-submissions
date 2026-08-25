class Solution:
    def numDecodings(self, s: str) -> int:
        
        if len(s) == 0:
            return 0 
        

        def dp(pos):
            if pos >= len(s):
                # reached the end of a valid path 
                return 1 
            
            if s[pos] == "0":
                return 0 # can't do anything with 0 
            
            if s[pos] == "1":
                if pos + 1 < len(s) and int(s[pos+1]) <= 9:
                    return dp(pos+1) + dp(pos+2)
            
            if s[pos] == "2":
                if pos + 1 < len(s) and int(s[pos+1]) <= 6:
                    return dp(pos+1) + dp(pos+2)
            
            return dp(pos+1)
        
        return dp(0)
            

