# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        l = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                l.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                l.append(None)
        print(l)
        ret = ""
        for pos, e in enumerate(l):
            ret += str(e) 
            if pos < len(l) - 1:
                ret += "," 
        print(ret)
        print(ret.split(","))
        return ret 
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        values = data.split(',')
        if values[0] == 'None':
            return None

        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1

        while queue and i < len(values):
            current = queue.pop(0)
            
            # Left child
            if values[i] != 'None':
                current.left = TreeNode(int(values[i]))
                queue.append(current.left)
            i += 1

            # Right child
            if i < len(values) and values[i] != 'None':
                current.right = TreeNode(int(values[i]))
                queue.append(current.right)
            i += 1

        return root 