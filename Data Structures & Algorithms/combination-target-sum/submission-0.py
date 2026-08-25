class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        solutions = []
        # def dfs(total, sol):
        #     # print(total, sol)
        #     for n in nums:
        #         if total + n == target:
        #             # found a solution 
        #             sol.append(n)
        #             solutions.append(sol)
        #         elif total + n < target:
        #             # could be a solution 
        #             dfs(total + n, sol + [n])
        # dfs(0, [])
        
        def dfs(sol, i, total):
            if (i+1 > len(nums)) or total > target:
                return 
            
            if total == target:
                solutions.append(sol.copy())
                return 

            sol.append(nums[i])
            dfs(sol, i, total + nums[i])
            sol.pop()
            dfs(sol, i+1, total)
        
        dfs([], 0, 0)
        return solutions
