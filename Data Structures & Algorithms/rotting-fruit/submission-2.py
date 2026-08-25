class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()

        visited = set()

        def addFruit(r, c):
            if min(r,c) < 0 or r >= len(grid) or c >= len(grid[0]) or (r,c) in visited or grid[r][c] != 1:
                return 
            visited.add((r,c))
            dq.append((r,c))


        fruits = 0
        # count the number of fruits 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    dq.append((r,c))
                elif grid[r][c] == 1:
                    fruits += 1
        
        if fruits == 0:
            return 0 
        
        minute = -1 
        while dq:
            # snapshot of size 
            n = len(dq)
            for i in range(n):
                r,c = dq.popleft()
                if grid[r][c] == 1:
                    grid[r][c] = 2 
                    fruits -= 1
                addFruit(r+1, c)
                addFruit(r-1, c)
                addFruit(r, c+1)
                addFruit(r, c-1)

            minute += 1 
        
        return minute if fruits == 0 else -1 