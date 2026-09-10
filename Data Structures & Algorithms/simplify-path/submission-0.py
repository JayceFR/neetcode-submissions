class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path += "/"
        for c in path:
            print("c", c)
            if c == "/":
                # two cases 
                # start, nothing in stack, so just add it
                # something before, we would need to evaluate it. 
                if not stack:
                    stack.append(c)
                    continue
                if stack[-1] == "/":
                    stack.pop() # solves the // case 
                prevTok = ""
                while stack and stack[-1] != "/":
                    prevTok = stack.pop() + prevTok
                if prevTok == "..":
                    # need to remove another prevToken
                    stack.pop() # Removes the / 
                    while stack and stack[-1] != "/":
                        stack.pop() # removes the previous token while keeping the / 
                elif prevTok == ".":
                    stack.pop() # remove the / 
                else:
                    # add it back to stack
                    for tok in prevTok:
                        stack.append(tok)

            if c != "/":
                stack.append(c)
            else:
                print("IN here")
                # check if previously we have a / 
                if stack == []:
                    stack.append(c)
                elif stack[-1] == "/":
                    continue
                else:
                    stack.append(c)
        if len(stack) > 1:
            stack.pop()
        retStr = ""
        for c in stack:
            retStr = retStr + c 
        return retStr
