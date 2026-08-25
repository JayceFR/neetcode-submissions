class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fp = 0 
        rp = 0 
        occur = {}
        maxOccur = 0 
        maxChar = ''
        maxLen = 0 
        while rp < len(s):
            if occur.get(s[rp]) is not None:
                occur[s[rp]] += 1 
            else:
                occur[s[rp]] = 1
            
            if occur[s[rp]] > maxOccur:
                maxOccur = occur[s[rp]]
                maxChar  = s[rp]

            # check if valid 
            length = rp - fp + 1 
            print("fp, rp", fp, rp)
            print("checking", s[fp : rp])
            # move fp till it becomes valid 
            while length - maxOccur > k:
                occur[s[fp]] -= 1 
                fp += 1 
                length = rp - fp + 1 
            maxLen = max(maxLen, length)
            rp += 1 
        return maxLen
        

            