class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([])
        nstr = str(n) # "19"
        s = 0
        while s != 1:
            s = 0 
            for c in nstr:
                ci = int(c)
                s += (ci * ci)
            print(s)
            if s in seen:
                return False 
            seen.add(s)
            nstr = str(s)
        return True
        