class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = ""
        length = 0
        for c in s:
            if c not in subs:
                subs += c
            else:
                # is present 
                # need to remove characters before c in subs
                subs = subs[subs.find(c)+1:]
                # add in c 
                subs += c 
            length = max(length, len(subs))
        return length 