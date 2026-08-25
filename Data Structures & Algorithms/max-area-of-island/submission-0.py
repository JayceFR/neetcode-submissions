class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
        print(visited)

        maxRs = len(grid)
        maxCs = len(grid[0])

        offset = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        def dfs(r, c, arr):
            nonlocal grid 
            visited[r][c] = True 
            
            for dr, dc in offset:
                nr = r + dr 
                nc = c + dc 

                if nr >= 0 and nr < maxRs and nc >= 0 and nc < maxCs:
                    if grid[nr][nc] == 1 and not visited[nr][nc]:
                        arr[0] += 1 
                        dfs(nr, nc, arr)
        
        islands = 0
        for r in range(maxRs):
            for c in range(maxCs):
                if grid[r][c] == 1 and not visited[r][c]:
                    l = [1]
                    dfs(r, c, l)
                    islands = max(islands, l[0])
        

        return islands 