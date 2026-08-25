class Solution:
    def minWindow(self, s: str, t: str) -> str:

        chars = {}
        for c in t:
            chars[c] = chars.get(c, 0) + 1 

        fp = 0 
        rp = 0 

        def windowValid(currMap):
            # check if items in chars are in currMap 
            for key, value in chars.items():
                if currMap.get(key) is None:
                    return False 
                if currMap[key] < value:
                    return False 
            return True 
            
        minLen = 1001
        minRp = 0 
        minFp = 0 
        currMap = {}
        match = False 
        while rp < len(s):
            ch = s[rp]
            currMap[ch] = currMap.get(ch, 0) + 1
            
            # check if window is valid 
            if windowValid(currMap):
                match = True 
                # update the minLen, minRp, minFp
                if (rp - fp + 1) < minLen:
                    minFp = fp 
                    minRp = rp 
                    minLen = rp - fp + 1 
                # now move the fp trying for another matching window
                cacheFp = fp 
                while windowValid(currMap) and fp <= rp:
                    currMap[s[fp]] -= 1 
                    fp += 1 
                # now reset it back 
                fp -= 1 
                currMap[s[fp]] += 1 
                if (rp - fp + 1) < minLen:
                    minFp = fp 
                    minRp = rp 
                    minLen = rp - fp + 1 

            rp += 1 
        if not match:
            return ""
        return s[minFp : minRp+1]
        