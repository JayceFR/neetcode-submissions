# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num = 0 

        def dfs(node, maxVal):
            if node is None:
                return 
            nonlocal num
            if node.val >= maxVal:
                num += 1 
            dfs(node.left, max(maxVal, node.val))
            dfs(node.right, max(maxVal, node.val))
        
        dfs(root, -101)

        return num