class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inbound = {}
        outbound = {}
        for t in trust:
            start, end = t[0], t[1]
            # start -> end 
            outbound[start] = outbound.get(start, 0) + 1 
            inbound[end] = inbound.get(end, 0) + 1 
        print(inbound)
        print(outbound)

        for k, v in inbound.items():
            if v == n - 1 and outbound.get(k, 0) == 0:
                return k 

        return -1  