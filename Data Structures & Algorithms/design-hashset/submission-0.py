class MyHashSet:
    # chaining 
    def __init__(self):
        self.buckets = [[]] * 1000

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.buckets[self._hash(key)].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.buckets[self._hash(key)].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[self._hash(key)]
    
    def _hash(self, key: int):
        return key % 1000 
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)