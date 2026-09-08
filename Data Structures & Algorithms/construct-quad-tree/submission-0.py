"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def recurs(sr, er, sc, ec) -> 'Node':
            # check if we need to split or not
            value = None
            same = True 
            for r in range(sr, er):
                for c in range(sc, ec):
                    if value is None:
                        value = grid[r][c]
                    else:
                        if value != grid[r][c]:
                            same = False 
            if same:
                return Node(val = True, isLeaf=True) if value == 1 else Node(val = False, isLeaf=True)
            # We need to break it up. 
            node = Node(isLeaf=False)
            midr = (sr + er) // 2 
            midc = (sc + ec) // 2 
            # Top left 
            node.topLeft = recurs(sr, midr, sc, midc)
            # Top right 
            node.topRight = recurs(sr, midr, midc, ec)
            # Bottom left 
            node.bottomLeft = recurs(midr, er, sc, midc)
            # Bottom right 
            node.bottomRight = recurs(midr, er, midc, ec)
            return node 

        ROWS, COLS = len(grid), len(grid[0])
        return recurs(0, ROWS, 0, COLS)
        
