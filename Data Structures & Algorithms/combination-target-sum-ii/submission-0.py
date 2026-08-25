class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        candidates.sort()
        def dfs(pos, sol, total):

            if total == target:
                solutions.append(sol.copy())
                return 

            if pos >= len(candidates):
                return 
            if total > target:
                return 
            

            sol.append(candidates[pos])
            dfs(pos + 1, sol, total + sol[-1])
            sol.pop()
            # check if we need to skip 
            
            while pos + 1 < len(candidates) and candidates[pos] == candidates[pos+1]:
                pos += 1 

            dfs(pos+1, sol, total)

        dfs(0, [], 0)
        return solutions 
            
