# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.ret = 0 
        def dfs(node):
            if node is None:
                return 0 
            ldepth = (1 + dfs(node.left))  if node.left else 0 
            rdepth = (1 + dfs(node.right)) if node.right else 0 
            
            self.ret = max(self.ret, ldepth + rdepth)


            return max(ldepth, rdepth) 
        
        dfs(root)

        return self.ret 
            