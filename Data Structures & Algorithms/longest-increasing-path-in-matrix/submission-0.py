class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        max_r = len(matrix) - 1
        max_c = len(matrix[0]) - 1

        memo = {}

        def dp(r, c):
            
            if (r,c) in memo:
                return memo[(r,c)]

            # valid 
            max_path_length = 1

            for dr, dc in offsets:
                new_r, new_c = r + dr, c + dc 

                if 0 <= new_r <= max_r and 0 <= new_c <= max_c and matrix[new_r][new_c] > matrix[r][c]:
                    max_path_length = max(max_path_length, 1 + dp(new_r, new_c))

            memo[(r,c)] = max_path_length 
            return memo[(r,c)]
        
        max_len = 0
        for r in range(max_r + 1):
            for c in range(max_c + 1):
                if (r,c) not in memo:
                    max_len = max(dp(r,c), max_len)
        
        return max_len 
