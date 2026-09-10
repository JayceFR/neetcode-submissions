class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "]":
                # We need to pop form our stack.
                repeatStr = ""
                while stack and stack[-1] != "[":
                    repeatStr = stack.pop() + repeatStr
                stack.pop() # Removes the "]"
                print("repeatstr", repeatStr)
                # Get the number 
                number = ""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                print("number", number)
                num = int(number)
                string = repeatStr * num 
                for c in string:
                    stack.append(c)
            else:
                stack.append(c)
        retString = ""
        for c in stack:
            retString += c 
        return retString
