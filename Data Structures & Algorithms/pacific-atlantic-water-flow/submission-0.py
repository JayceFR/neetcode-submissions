class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited = set()

        pacific = set()
        atlantic = set()

        dq = deque()

        maxRs = len(heights)
        maxCs = len(heights[0]) if maxRs > 0 else 0

        def addDqPacific(r, c, h):
            if min(r,c) < 0 or r >= maxRs or c >= maxCs or h > heights[r][c] or (r,c) in visited:
                return
            pacific.add((r,c))
            visited.add((r,c))
            dq.append((r,c))

        def addDqAtlantic(r, c, h):
            if min(r,c) < 0 or r >= maxRs or c >= maxCs or h > heights[r][c] or (r,c) in visited:
                return
            atlantic.add((r,c))
            visited.add((r,c))
            dq.append((r,c))

        # add first row 
        for c in range(maxCs):
            dq.append((0,c))
            visited.add((0,c))
            pacific.add((0,c))
        
        # add first column 
        for r in range(maxRs):
            if (r,0) not in visited:
                dq.append((r,0))
                visited.add((r,0))
                pacific.add((r,0))
        
        # bfs 
        while dq:
            (r,c) = dq.popleft()
            h = heights[r][c]
            addDqPacific(r+1, c, h)
            addDqPacific(r-1, c, h)
            addDqPacific(r, c+1, h)
            addDqPacific(r, c-1, h)
        
        visited = set()
        dq = deque()

        # add last row 
        for c in range(maxCs):
            dq.append((maxRs-1,c))
            visited.add((maxRs-1, c))
            atlantic.add((maxRs-1,c))
        
        # add last column 
        for r in range(maxRs):
            if (r, maxCs-1) not in visited:
                dq.append((r, maxCs-1))
                visited.add((r, maxCs-1))
                atlantic.add((r, maxCs-1))
        
        while dq:
            (r,c) = dq.popleft()
            h = heights[r][c]
            addDqAtlantic(r+1, c, h)
            addDqAtlantic(r-1, c, h)
            addDqAtlantic(r, c+1, h)
            addDqAtlantic(r, c-1, h)

        print("pacific", pacific)
        print("atlantic", atlantic)
        
        return list(map(lambda x : list(x) ,atlantic.intersection(pacific)))