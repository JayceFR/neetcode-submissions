class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        pars = [x for x in range(n+1)]
        ranks = [1 for x in range(n+1)]

        def find(node):
            if node == pars[node]:
                return node 
            pars[node] = pars[pars[node]]
            return find(pars[node])
               
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return True 
            
            if ranks[p2] > ranks[p1]:
                pars[p1] = p2
                ranks[p2] += ranks[p1]
            else:
                pars[p2] = p1
                ranks[p1] += ranks[p2]

            return False 
        
        for n1, n2 in edges:
            if union(n1,n2):
                return [n1, n2]

        return []
            