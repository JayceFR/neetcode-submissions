# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # I see a recursive solution to this problem 
        # its going to have 2 cases
        # 1. If the node.val == target and is a leaf node, then we just return None 
        # 2. If the node.val == target and is not a leaf node, then we set its right and left recursively, and then at the end we check if they both are None, then we return None 
        # 3. Otherwise we just populate through 

        def dfs(curr: Optional[TreeNode]) -> Optional[TreeNode]:
            if curr is None:
                return None 
            
            if curr.val == target:
                if curr.left is None and curr.right is None:
                    # leaf 
                    return None 
                else:
                    curr.left = dfs(curr.left)
                    curr.right = dfs(curr.right)
                    if curr.left is None and curr.right is None:
                        return None 
            else:
                curr.left = dfs(curr.left)
                curr.right = dfs(curr.right)
            return curr 
        
        return dfs(root)
