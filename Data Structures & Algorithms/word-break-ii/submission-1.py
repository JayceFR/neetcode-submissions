class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # It looks a normal backtracking problem at first glance. 
        # I don't know the recommended time complexity. 
        # But im thinking of just looking through words in the dict and then check if s is starting with it. 
        # if it is then we just split it up. 
        # the length of word dict is quite long, so might be the root cause of the problem being a hard 

        res = []

        dic = set(wordDict)

        curr_res = []

        def recurs(c : str):
            if len(c) == 0:
                # found a solution 
                res.append(" ".join(curr_res))
                return 
            for word in dic:
                if c.startswith(word):
                    curr_res.append(word)
                    recurs(c[len(word):])
                    curr_res.pop()
        
        recurs(s)

        # it passed?? HOW IS THIS HARD?

        return res 