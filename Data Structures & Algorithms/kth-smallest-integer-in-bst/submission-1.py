# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def traverse(self, curr, visited, k):
        if curr.left:
            val = self.traverse(curr.left, visited, k) 
            if val is not None:
                return val 
        k[0] -= 1 
        if k[0] == 0:
            return curr.val 
        if curr.right:
            val = self.traverse(curr.right, visited, k)
            if val is not None:
                return val 

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = []
        return self.traverse(root, visited, [k])
        # return visited[k-1]
        