class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }

        if digits == "":
            return []

        pad = []
        for letter in digits:
            pad.append(phone[letter])
        
        print(pad)

        sols = []

        def dfs(sol, pos):
            if pos == len(digits):
                sols.append(sol)
                return 
            
            for letter in pad[pos]:
                dfs(sol + letter, pos + 1)
        
        dfs("", 0)

        return sols 

