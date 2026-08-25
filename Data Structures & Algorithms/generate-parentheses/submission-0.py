class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parens = []

        def gen(m, opens, currStr):
            if m == 0:
                # we have added everything, time to close 
                currStr += (')' * opens)
                parens.append(currStr)
            else:
                # we have an option, either close if possible or open
                if opens:
                    # close 
                    gen(m, opens - 1, currStr + ')')
                # open 
                gen(m-1, opens + 1, currStr + '(')
        
        gen(n, 0, "")
        return parens 