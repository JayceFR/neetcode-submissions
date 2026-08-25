class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # ready the hashmap 
        chars = {}
        for c in s1:
            chars[c] = chars.get(c, 0) + 1 
        print(chars)

        if len(s2) < len(s1):
            return False 

        #sliding window 
        fp = 0 
        rp = len(s1) - 1 

        def checkWindow(fp, rp):
            newMap = {}
            for x in range(fp, rp+1):
                currCh = s2[x]
                newMap[currCh] = newMap.get(currCh, 0) + 1 
            return newMap == chars 
                


        while rp < len(s2):

            # check if window is valid 
            for x in range(fp, rp+1):
                value = checkWindow(fp, rp)
                if value == True:
                    return True  
                

            fp += 1 
            rp += 1 


        return False  