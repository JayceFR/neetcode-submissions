# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        #VLR
        res = []
        
        def dfs(node, depth):
            if node is None:
                return 
            #visit
            nonlocal res 
            if len(res) <= depth:
                res.append([])
            res[depth].append(node.val)
            #left 
            dfs(node.left, depth + 1)
            #right 
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        ans = []
        for r in res:
            ans.append(r[len(r) - 1])
        return ans 