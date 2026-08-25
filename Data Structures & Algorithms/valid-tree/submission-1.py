class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj_matrix = {}
        for x in range(n):
            adj_matrix[x] = []
        
        
        for n1,n2 in edges:
            # undirected graph 
            adj_matrix[n1].append(n2)
            adj_matrix[n2].append(n1)

        visited = set()

        def dfs(curr, prev):
            
            visited.add(curr)

            neighs = adj_matrix[curr] 
            if prev is not None:
                neighs.remove(prev)

            for n in neighs:
                if n in visited:
                    return False 
                if dfs(n, curr) == False:
                    return False
                 
            return True 

        # cycle detection 
        if dfs(0,None) == False:
            return False 
        
        # connected 
        for x in range(n):
            if x not in visited:
                return False 
        
        return True 

