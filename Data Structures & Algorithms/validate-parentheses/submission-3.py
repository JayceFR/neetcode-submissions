class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False 
        
        chars = {
            '(' : ')', 
            '{' : '}',
            '[' : ']' 
        }

        stack = []

        for pos, c in enumerate(s):
            if chars.get(c) is not None:
                # c is open bracket 
                stack.append(c)
            else:
                if not stack:
                    return False 
                lastOpen = stack.pop(len(stack)-1)
                if c != chars[lastOpen]:
                    return False

        return stack == []
