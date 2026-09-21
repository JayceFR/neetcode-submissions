class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i, c in enumerate(order):
            dic[c] = i 
        for x in range(1, len(words)):
            prev = words[x-1]
            curr = words[x]

            pp = 0 
            cp = 0 

            while pp < len(prev) and cp < len(curr) and prev[pp] == curr[cp]:
                pp += 1 
                cp += 1 
            
            if pp < len(prev):
                if cp == len(curr): # size difference case
                    return False 
                if dic[prev[pp]] > dic[curr[cp]]:
                    return False 

        return True 