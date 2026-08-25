class LRUCache:

    def __init__(self, capacity: int):
        self.size     = 0 
        self.capacity = capacity 
        self.cache    = {}
        self.time     = 0 

    def get(self, key: int) -> int:
        if self.cache.get(key) is None:
            return -1 
        # update the usage 
        self.cache[key] = (self.cache[key][0], self.time )
        self.time += 1 
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key) is None:
            self.size += 1 
            if self.size > self.capacity:
                # remove the LRU item  
                term = [0, float("infinity")]
                for k, v in self.cache.items():
                    if v[1] < term[1]:
                        term = [k, v[1]]
                del self.cache[term[0]]
                self.size -= 1 
        self.cache[key] = (value, self.time)
        self.time += 1 

