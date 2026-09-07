# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            return node
        def insert(curr):
            if val > curr.val:
                if curr.right:
                    insert(curr.right)
                else:
                    curr.right = node 
            else:
                if curr.left:
                    insert(curr.left)
                else:
                    curr.left = node
        insert(root)
        return root
            