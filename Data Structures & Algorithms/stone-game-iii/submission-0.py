class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        '''
        Keep track of alice score 
        Alice would want to maximise her score 
        Bob would want to minimise Alice's score 

        We can do the minimax 
        [2,4,3,1,2]

        But neetcode the goat, suggests a different way of modelling the entire problem 

        Let dp[i] be by how much can whoseever turn it is win by starting at i
        So take [2,4,3,1]
        lets say i = 0, we can take 2, then the opponent would get 4+3+1 = 8. So we are loosing, which is modelled as 2 - 8 = -6 
        We would want to maximise that. 

        TOO SMART!

        Now we can obviously space optimise this solution as well.
        '''

        dp = [0] * 3

        for i in range(len(stoneValue) - 1, -1, -1):
            total = 0 
            res = -10001
            for j in range(i, min(i+3, len(stoneValue))):
                total += stoneValue[j]
                res = max(res, total - dp[(j+1) % 3])
            dp[i%3] = res 
        
        if dp[0] == 0:
            return "Tie"
        return "Alice" if dp[0] > 0 else "Bob"