class Solution:
    def solve(self, board: List[List[str]]) -> None:
        start_pos = []
        maxRs = len(board)
        maxCs = len(board[0])

        visited = set()

        for c in range(maxCs):
            if board[0][c] == "O":
                start_pos.append((0,c))
            if board[maxRs-1][c] == "O":
                start_pos.append((maxRs-1, c))
        
        for r in range(maxRs):
            if board[r][0] == "O":
                start_pos.append((r,0))
            if board[r][maxCs-1] == "O":
                start_pos.append((r,maxCs-1))
        
        offsets = [(0,1), (1,0), (0,-1), (-1,0)]
        # now dfs from each of these border 0s 
        def dfs(r, c):
            visited.add((r,c))
            for dr,dc in offsets:
                row = r + dr 
                col = c + dc 

                if min(row, col) >= 0 and row < maxRs and col < maxCs and board[row][col] == "O" and (row,col) not in visited:
                    # then dfs from there 
                    dfs(row, col)
        
        for r,c in start_pos:
            if (r,c) not in visited:
                dfs(r,c)    
        
        print(visited)

        for r in range(maxRs):
            for c in range(maxCs):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"
            