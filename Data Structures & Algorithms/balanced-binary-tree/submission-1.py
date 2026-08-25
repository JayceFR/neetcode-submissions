# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.res = True 
        def dfs(node):
            if node is None:
                return 0 
            lh = (1 + dfs(node.left))  if node.left else 0
            rh = (1 + dfs(node.right)) if node.right else 0 

            if self.res:
                if abs(lh - rh) > 1:
                    self.res = False 

            return max(lh, rh)
        dfs(root)
        return self.res 