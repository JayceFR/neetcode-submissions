# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def search(node, val):
            if node is None:
                return False 
            if node.val == val:
                return True 
            return search(node.left, val) or search(node.right, val)
        
        def dfs(node):

            if node is None:
                return None 

            lp = search(node.left, p.val)
            rp = search(node.right, p.val)
            lq = search(node.left, q.val)
            rq = search(node.right, q.val)

            if (lp and rq) or (rp and lq):
                # we found the answer
                return node 
            
            if ((node.val == p.val) and (lq or rq)) or ((node.val == q.val) and (lp or rp)):
                # we again found the answer
                return node 
            
            # look left 
            ans = dfs(node.left)
            if ans != None:
                return ans 
            
            # look right 
            ans = dfs(node.right)
            if ans != None:
                return ans 
            
            return None 
        
        return dfs(root)
            

            