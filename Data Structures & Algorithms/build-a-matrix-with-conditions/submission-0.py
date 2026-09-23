class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Topological sort Graph PROBLEM! How can i come up with this, without knowing its a graph problem in 20 mins??? 

        def dfs(src, adj, visited, path, order):
            # dfs to the end and add the last element. 
            # cycle check 
            if src in path:
                return False 
            if src in visited:
                return True 

            visited.add(src)
            path.add(src)

            for nei in adj[src]:
                if not dfs(nei, adj, visited, path, order):
                    return False 

            path.remove(src)

            order.append(src)           

            return True 

        
        def topoSort(edges):
            # Build adjacency graph 

            adj = defaultdict(list)
            for src, dst in edges:
                adj[src].append(dst)

            visited = set()
            path = set()
            order = [] 
            for src in range(1, k+1):
                if src not in visited:
                    if not dfs(src, adj, visited, path, order):
                        return []
            return order[::-1]

        row_order = topoSort(rowConditions)
        if not row_order: return []
        
        col_order = topoSort(colConditions)
        if not col_order: return []

        val_to_row = {num : i for i, num in enumerate(row_order)}
        val_to_col = {col: i for i, col in enumerate(col_order)}

        res = [[0] * k for _ in range(k)]

        for num in range(1, k+1):
            r,c = val_to_row[num], val_to_col[num] 
            res[r][c] = num 
        
        return res 