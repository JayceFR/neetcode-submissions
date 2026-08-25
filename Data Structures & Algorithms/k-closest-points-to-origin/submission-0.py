import heapq as h 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            dist = math.sqrt(p[0] * p[0] + p[1] * p[1])
            h.heappush(heap, (dist, p[0], p[1]))
        res = []
        for x in range(k):
            val, x, y = h.heappop(heap)
            res.append([x,y])
        return res 
