class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False for x in range(numCourses)]

        adj_matrix = {}

        for x in range(numCourses):
            adj_matrix[x] = []

        for f,s in prerequisites:
            adj_matrix[s].append(f)
        
        print(adj_matrix)

        def dfs(curr, depends):
            depends.append(curr)
            for x in adj_matrix[curr]:
                if x in depends:
                    return False 
                if dfs(x, depends.copy()) == False:
                    return False 
            return True 

        for x in range(numCourses):
            if dfs(x, []) == False:
                return False 
        return True 