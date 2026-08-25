class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        def checkValidPrefix(pr):
            for s in strs:
                if not s.startswith(pr):
                    return False 
            return True 

        fs = strs[0]

        if not fs:
            return ""

        prev_pre = ""
        curr_pre = fs[0]
        pos = 1
        while checkValidPrefix(curr_pre):
            print("In here")
            prev_pre = curr_pre
            
            if pos >= len(fs):
                return curr_pre 
                
            curr_pre += fs[pos]
            pos += 1 
        
        return prev_pre 
