class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # p is the pointer to text 1 and q to text 2 
        # time complexity is O(2^(len(text1) + len(text2)))
        # def dp(p, q): 
        #     if p >= len(text1) or q >= len(text2):
        #         return 0 
            
        #     if text1[p] == text2[q]:
        #         return 1 + dp(p+1, q+1)
            
        #     return max(dp(p+1, q), dp(p,q+1))
        
        # return dp(0,0)

        # we can do better :)
        memo = {}
        def dp(p, q): 
            if p >= len(text1) or q >= len(text2):
                return 0 
            
            if (p,q) in memo:
                return memo[(p,q)]
            

            if text1[p] == text2[q]:
                memo[(p,q)] = 1 + dp(p+1, q+1)
                return memo[(p,q)]
            
            memo[(p,q)] = max(dp(p+1, q), dp(p,q+1))
            return memo[(p,q)]
        
        return dp(0,0)
