# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mp = -1001

        def dfs(node):
            if node is None:
                return 0
            val = node.val 
            lval = dfs(node.left)
            rval = dfs(node.right)
            mval = max(val, max(val + rval, max(val + lval + rval, val + lval)))
            nonlocal mp 
            mp = max(mp, mval)
            return max(val, val + max(rval, lval))

        dfs(root)
        return mp 
