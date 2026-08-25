class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        curr = nums.pop(0)
        rest = self.permute(nums)

        sol = []
        for r in rest:
            for x in range(len(r) + 1):
                rCopy = r.copy()
                rCopy.insert(x, curr)
                sol.append(rCopy)
        
        return sol