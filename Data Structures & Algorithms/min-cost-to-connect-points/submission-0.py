class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        visit = [False] * n
        dist = [float('inf')] * n
        dist[0] = 0

        res = 0

        for _ in range(n):
            # Find cheapest unvisited node
            node = -1
            for i in range(n):
                if not visit[i] and (node == -1 or dist[i] < dist[node]):
                    node = i

            visit[node] = True
            res += dist[node]

            # Update cheapest connection for every unvisited node
            for i in range(n):
                if not visit[i]:
                    cost = abs(points[i][0] - points[node][0]) + \
                           abs(points[i][1] - points[node][1])

                    dist[i] = min(dist[i], cost)

        return res