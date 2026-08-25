# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(np, nq):
            if not np and not nq:
                return True
            if np and nq and np.val == nq.val:
                return dfs(np.left, nq.left) and dfs(np.right, nq.right)
            else:
                return False 
        
        return dfs(p, q)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True 
        if not root:
            return False 

        if self.isSameTree(root, subRoot):
            return True 
        return (self.isSubtree(root.left, subRoot)) or self.isSubtree(root.right, subRoot)
            




