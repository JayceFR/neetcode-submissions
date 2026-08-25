import heapq as h 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        h.heapify(heap)

        while len(heap) > 1:
            x = -h.heappop(heap)
            y = -h.heappop(heap)
            if x < y:
                h.heappush(heap, -(y - x))
            if y < x:
                h.heappush(heap, -(x - y))
        return -heap[0] if heap else 0 