# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(np, nq):
            if np is None and nq is None:
                return True 
            else:
                if np is None or nq is None:
                    return False 
        
            if np.val != nq.val:
                return False 
            
            res = True 
            if np.left and nq.left:
                res = (res and dfs(np.left, nq.left))
            else:
                if np.left or nq.left:
                    return False 
            
            if np.right and nq.right:
                res = (res and dfs(np.right, nq.right))
            else:
                if np.right or nq.right:
                    return False 
            
            return res 
        
        return dfs(p, q)