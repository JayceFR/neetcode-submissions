# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        self.depth = 1 
        def dfs(node, d):
            self.depth = max(self.depth, d)
            if node.left:
                dfs(node.left, d+1)
            if node.right:
                dfs(node.right, d+1)
        dfs(root, self.depth)
        return self.depth 
                