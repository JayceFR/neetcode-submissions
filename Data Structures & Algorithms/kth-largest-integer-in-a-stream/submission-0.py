import heapq as h 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.heap = nums
        h.heapify(self.heap)
        while len(self.heap) > self.k:
            h.heappop(self.heap)

    def add(self, val: int) -> int:
        h.heappush(self.heap, val)
        while len(self.heap) > self.k: 
            h.heappop(self.heap)
        return self.heap[0] 
