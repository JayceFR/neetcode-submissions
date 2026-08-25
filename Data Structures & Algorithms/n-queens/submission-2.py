class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["." * n for _ in range(n)]
        sols = []

        def isValid(game, row, col):
            # check col
            for r in range(row):
                if game[r][col] == 'Q':
                    return False
            # check diag ↖
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if game[r][c] == 'Q':
                    return False
                r -= 1; c -= 1
            # check diag ↗
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if game[r][c] == 'Q':
                    return False
                r -= 1; c += 1
            return True

        def dfs(row):
            if row == n:
                sols.append(board.copy())
                return
            for col in range(n):
                if isValid(board, row, col):
                    board[row] = "." * col + "Q" + "." * (n - col - 1)
                    dfs(row + 1)
                    board[row] = "." * n  # reset row

        dfs(0)
        return sols
