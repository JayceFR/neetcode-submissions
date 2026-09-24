class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False for x in range(numCourses)]

        adj_matrix = {}

        for x in range(numCourses):
            adj_matrix[x] = []

        for f,s in prerequisites:
            adj_matrix[s].append(f)
        
        print(adj_matrix)

        # Old inefficient code written by the small young Jayce!
        
        # def dfs(curr, depends):
        #     depends.append(curr)
        #     for x in adj_matrix[curr]:
        #         if x in depends:
        #             return False 
        #         if dfs(x, depends.copy()) == False:
        #             return False 
        #     return True 
        # for x in range(numCourses):
        #     if dfs(x, []) == False:
        #         return False 

        # New code written by the old Jayce. Ahh my back hurts!

        # We only need to do a cycle detection here. 
        visited = [0] * numCourses
        def dfs(curr):
            
            if visited[curr] == 1:
                return False 
            
            if visited[curr] == 2: # already checked 
                return True

            visited[curr] = 1 

            for x in adj_matrix[curr]:
                if not dfs(x):
                    return False 

            visited[curr] = 2 
            return True 
        
        for x in range(numCourses):
            if dfs(x) == False:
                return False 
        
        return True 