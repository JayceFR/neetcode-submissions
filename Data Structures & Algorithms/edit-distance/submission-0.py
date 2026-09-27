class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        Let dp[i][j] be the minimum number of operations to make word1[i:] equal to word2[j:]

        dp[i][j] | i >= len(word1)      => len(word2) - j 
                 | j >= len(word2)      => 0 
                 | word1[i] == word2[j] => min(dp[i+1][j+1], 1+dp[i+1, j]) # we accept or delete 
                 | else                 => min(1 + dp[i+1][j+1], 1 + dp[i][j+1], 1 + dp[i+1][j]) # replace, insert or delete 
        '''

        # Bottom up solution space optimise with keeping track of 1 row. 

        I, J = len(word1), len(word2)

        dp = [0] * (J+1)
        for j in range(J):
            dp[j] = J - j 
        
        for i in range(I-1, -1, -1):
            new_dp = [0] * (J+1)

            new_dp[J] = I-i
            
            for j in range(J-1, -1, -1):
                if word1[i] == word2[j]:
                    new_dp[j] = min(dp[j+1], 1+dp[j])
                else:
                    new_dp[j] = min(1 + dp[j+1], 1 + new_dp[j+1], 1 + dp[j])

            dp = new_dp

        return dp[0]