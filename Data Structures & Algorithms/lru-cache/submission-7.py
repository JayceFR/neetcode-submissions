'''
Need to keep track of the order of entry, so a list. 
But a normal python list would give us O(n) to remove. 
Instead we make our own doubly linked list and store the node in a map. 
So Now we can efficiently remove from the doubly linked list. 
'''

class Node:
    def __init__(self, key, val, nex = None, prev = None) -> None:
        self.key = key 
        self.val = val 
        self.nex = nex 
        self.prev = prev 

class DL:
    def __init__(self) -> None:
        self.root = Node(-1, -1) # Keeps track of LRU
        self.end = self.root # Keeps track of MRU 
    def add(self,node): # O(1)
        self.end.nex = node 
        node.prev = self.end 
        node.nex = None
        self.end = node 
    def remove(self, node): # O(1)
        parent = node.prev 
        parent.nex = node.nex  
        if node.nex:
            node.nex.prev = parent
        if node == self.end: # fix end 
            self.end = parent
        node.prev = None 
        node.nex = None 
    def lru(self):
        if self.root.nex is None:
            raise ValueError("Shouldn't be null here")
        return self.root.nex
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0 
        self.dl = DL()
        self.nodeMap = {} # key to Node 

    def get(self, key: int) -> int:
        if key in self.nodeMap:
            # We would need to still remove and pop 
            node = self.nodeMap[key]
            self.dl.remove(node)
            self.dl.add(node) # Moves it to MRU 
            return node.val 
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            # Need to update the value 
            node = self.nodeMap[key]
            self.dl.remove(node)
            node.val = value 
            self.dl.add(node)
        else:
            # adding a new value, so need to check size 
            if self.size == self.cap:
                # Need to evict something 
                lru_node = self.dl.lru()
                self.dl.remove(lru_node)
                del self.nodeMap[lru_node.key]
                self.size -= 1 
            # size is present, create the node 
            node = Node(key, value)
            self.dl.add(node)
            self.nodeMap[key] = node 
            self.size += 1 
