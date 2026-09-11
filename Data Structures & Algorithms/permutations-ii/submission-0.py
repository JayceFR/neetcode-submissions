class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        def backtrack(numbers : List[int], perm: List[int]):
            if len(numbers) == 0:
                res.append(perm.copy())
                return 
            
            curr = None
            for i in range(len(numbers)):
                if curr is not None and curr == numbers[i]:
                    # skip, to avoid duplicates
                    continue
                curr = numbers[i]
                perm.append(curr)
                copy = numbers.copy()
                copy.remove(curr)
                backtrack(copy, perm)
                perm.pop()
        backtrack(nums, [])
        return res 