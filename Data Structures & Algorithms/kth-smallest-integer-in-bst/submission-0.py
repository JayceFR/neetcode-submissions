# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def traverse(self, curr, visited):
        if curr.left:
            self.traverse(curr.left, visited)
        visited.append(curr.val)
        if (curr.right):
            self.traverse(curr.right, visited)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = []
        self.traverse(root, visited)
        return visited[k-1]
        