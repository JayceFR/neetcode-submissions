class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''

        okens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

        (( 10 * ( 6 / ( (9 + 3) * -11))) + 17) + 5 

        '''
    
        operators = ['+', '-', '*', '/']

        def evaluate(tokens):
            tok = tokens.pop()
            if tok in operators:
                # handle the operation case 
                re, rtoks = evaluate(tokens)
                le, ltoks = evaluate(rtoks)
                if tok == '+':
                    # print(le, "+", re)
                    return (le + re, ltoks)
                elif tok == '-':
                    # print(le, "-", re)
                    return (le - re, ltoks)
                elif tok == '*':
                    # print(le, '*', re)
                    return (le * re, ltoks)
                else:
                    # print(le, '//', re)
                    return (int(le / re), ltoks)
            else:
                # its a number 
                return (int(tok), tokens)

        return evaluate(tokens)[0]

        