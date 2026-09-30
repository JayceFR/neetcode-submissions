import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        # Code written by old Jayce, it does work, but timesout for leetcode. 

        # def dfs(x, y, level):
        #     if x == n - 1 and y == n - 1:
        #         return level

        #     visited[x * n + y] = True
        #     level = max(level, grid[x][y])
        #     min_level = n * n

        #     for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        #         nx, ny = x + dx, y + dy
        #         if 0 <= nx < n and 0 <= ny < n and not visited[nx * n + ny]:
        #             visited[nx * n + ny] = True
        #             min_level = min(min_level, dfs(nx, ny, max(level, grid[nx][ny])))
        #             visited[nx * n + ny] = False

        #     return min_level

        # n = len(grid)
        # visited = [False] * (n * n)
        # visited[0] = True
        # return dfs(0, 0, grid[0][0])

        # New Jayce thinks bfs would be a better solution. 
        # Use a heap to store the value and with that we would be popping the lowest element. 
        # We would obviously need to keep track of visited, which we would only add to, but not remove from. 
        # We need the visited to make sure we are not adding duplicates in the heap. 
        # Should be O(n^2 * (log n)) time complexity

        heap = [] # key -> (level, x, y)
        n = len(grid)
        visited = [False] * (n * n)

        heapq.heappush(heap, (grid[0][0], 0, 0))
        level = 0 
        while heap:
            l, x, y = heapq.heappop(heap)
            level = max(level, l)
            if x == n-1 and y == n-1:
                return level 
            for dx, dy in [[0,1], [1,0], [-1, 0], [0,-1]]:
                nx, ny = x + dx, y + dy 
                if 0 <= nx < n and 0 <= ny < n and not visited[nx * n + ny]:
                    visited[nx * n + ny] = True 
                    heapq.heappush(heap, (grid[nx][ny], nx, ny))

        return 0 
