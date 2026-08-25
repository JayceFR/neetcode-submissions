class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1 
        n = len(matrix[0]) - 1 if m >= 0 else 0 

        def bs(fp, rp): 
            if fp[0] < 0 or fp[1] < 0 or fp[0] > m or fp[1] > n:
                return False 
            if rp[0] < 0 or rp[1] < 0 or rp[0] > m or rp[1] > n:
                return False 
            start = fp[0] * (n+1) + fp[1]
            end   = rp[0] * (n+1) + rp[1]
            if start > end:
                return False 
            mid   = (start + end) // 2 
            mp = [mid // (n+1), mid % (n+1)]
            if matrix[mp[0]][mp[1]] < target: 
                mid = start + 1 
                new = [mid // (n+1), mid % (n+1)]
                return bs(new, rp)
            elif matrix[mp[0]][mp[1]] > target:
                mid = end - 1 
                new = [mid // (n+1), mid % (n+1)]
                return bs(fp, new)
            else:
                return True 
        return bs([0,0], [m,n])