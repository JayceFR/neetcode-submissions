class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.strip()
        newS = ""
        for c in s:
            if c.isalnum():
                newS += c 
        lp = 0 
        rp = len(newS) - 1
        while lp < rp:
            if newS[lp].lower() == newS[rp].lower():
                lp += 1
                rp -= 1
            else:
                return False 
        '''
        abcba
        abccba
        '''
        return True
        