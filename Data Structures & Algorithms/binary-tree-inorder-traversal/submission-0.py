# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # LVR
        retList = []
        def dfs(curr: TreeNode):
            if not curr:
                return 
            if curr.left:
                dfs(curr.left)
            retList.append(curr.val)
            if curr.right:
                dfs(curr.right)
        dfs(root)
        return retList 