import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def hrs(k):
            hr = 0 
            for p in piles:
                hr += math.ceil(p / k)
            return hr 

        rp = max(piles)
        fp = 1

        cacheK = rp
        while fp <= rp:
            k  = (fp + rp) // 2
            hr = hrs(k)
            if hr > h:
                fp = k + 1 
            else:
                cacheK = min(cacheK, k)
                rp = k - 1 
        return cacheK