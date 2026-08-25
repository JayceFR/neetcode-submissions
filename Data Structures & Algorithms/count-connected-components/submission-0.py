class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
                if n not in visited:
                    dfs(n, curr)

        comps = 0 
        dfs(0, None)
        comps += 1 
           
        # connected 
        for x in range(n):
            if x not in visited:
                comps += 1 
                dfs(x, None)
        return comps 
            