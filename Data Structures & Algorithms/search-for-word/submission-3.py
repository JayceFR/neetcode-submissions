class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        offsets = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        rows = len(board)
        cols = len(board[0]) if len(board) > 0 else 0

        def withinbounds(pos):
            nonlocal rows, cols 
            return pos[0] >= 0 and pos[0] < rows and pos[1] >= 0 and pos[1] < cols

        def dfs(string, curr, visited):

            string += board[curr[0]][curr[1]]
            # if string[len(string) - 1] != word[len(string) - 1]:
            #     return False

            print(curr, string)

            if string == word:
                return True 
            
            if len(string) >= len(word):
                return False 
            
            for offset in offsets: 
                curr[0] += offset[0]
                curr[1] += offset[1]
                
                if withinbounds(curr) and not visited[curr[0]][curr[1]]:
                    visited[curr[0]][curr[1]] = True 
                    ret = dfs(string, curr, visited)
                    visited[curr[0]][curr[1]] = False 
                    if ret == True:
                        return True 

                curr[0] -= offset[0]
                curr[1] -= offset[1]
            
            return False 
        
        visited = [[False for x in range(cols)] for y in range(rows)]
        for y in range(rows):
            for x in range(cols):
                curr = [y, x]
                visited[curr[0]][curr[1]] = True 
                if dfs("", curr, visited):
                    return True 
                visited[curr[0]][curr[1]] = False 
        return False 

