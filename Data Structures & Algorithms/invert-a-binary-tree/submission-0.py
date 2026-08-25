# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(node):
            if node is None: 
                return None
            nleft  = invert(node.left)  if node.left else None 
            nright = invert(node.right) if node.right else None 

            node.left  = nright 
            node.right = nleft 
            return node
        
        return invert(root)