class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # [1,2,3]
        # k = 1 
        # [1] , [2] , [3]
        res = []
        def backtrack(curr: int, h:int, comb: List[int]):
            if curr > n:
                return 
            if h > k:
                return 
            if h == k:
                # found an answer 
                res.append(comb + [curr])
        
            comb.append(curr)
            backtrack(curr+1, h+1, comb)
            comb.pop()

            backtrack(curr+1, h, comb)

        backtrack(1, 1, [])
        return res 

