class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sols = []
        nums.sort()
        def dfs(sol, pos):
            if pos == len(nums):
                sols.append(sol.copy())

            if pos >= len(nums):
                return 

            sol.append(nums[pos])
            dfs(sol, pos + 1)
            sol.pop()

            while pos + 1 < len(nums) and nums[pos + 1] == nums[pos]:
                pos = pos + 1 
            dfs(sol, pos + 1)

        dfs([], 0)

        return sols