# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # VLR 
        retList = []
        def dfs(curr: TreeNode):
            if not curr:
                return 
            retList.append(curr.val)
            dfs(curr.left)
            dfs(curr.right)
        dfs(root)
        return retList 