import heapq as h 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = {}

        for node in range(n+1):
            adj_list[node] = []

        for u, v, t in times:
            adj_list[u].append((t,v))

        heap = [(0, k)]

        visited = set()
        maxTime = 0
        while heap:
            currTime, node = h.heappop(heap)
            if node not in visited:
                maxTime = max(maxTime, currTime)
                visited.add(node)
                for t, v in adj_list[node]:
                    if v not in visited:
                        h.heappush(heap, (currTime + t, v))

        return maxTime if len(visited) == n else -1
