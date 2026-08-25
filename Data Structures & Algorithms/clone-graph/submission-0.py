"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = {}
        def dfs(node):
            nonlocal visited 
            if node is None:
                return None 
            # check if already created
            nodeCopy = Node(node.val)
            visited[node] = nodeCopy
            for n in node.neighbors:
                if n in visited:
                    nodeCopy.neighbors.append(visited[n])
                else:
                    nodeCopy.neighbors.append(dfs(n))
            return nodeCopy 
        
        return dfs(node)
                
            


        # if node is None:
        #     return None 
        # node_copy = Node(node.val)
        # for n in node.neighbors:
        #     node_copy.neighbors.append(self.cloneGraph(n))
        # return node_copy