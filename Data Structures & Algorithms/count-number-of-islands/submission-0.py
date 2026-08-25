class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
        print(visited)
        noOfIslands = 0 

        maxRs = len(grid)
        maxCs = len(grid[0])

        offset = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        def dfs(r, c):
            nonlocal grid 
            visited[r][c] = True 
            
            for dr, dc in offset:
                nr = r + dr 
                nc = c + dc 

                if nr >= 0 and nr < maxRs and nc >= 0 and nc < maxCs:
                    if grid[nr][nc] == "1" and not visited[nr][nc]:
                        dfs(nr, nc)
            
        for r in range(maxRs):
            for c in range(maxCs):
                if grid[r][c] == "1" and not visited[r][c]:
                    noOfIslands += 1
                    dfs(r, c)
        

        return noOfIslands 