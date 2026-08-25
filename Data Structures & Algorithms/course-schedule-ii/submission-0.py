class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_matrix = {}
        for x in range(numCourses):
            adj_matrix[x] = []
        
        for f,s in prerequisites:
            adj_matrix[s].append(f)      

        path = deque()

        visited = set()

        def topo(curr, cycle):
            visited.add(curr)

            cycle.add(curr)

            for x in adj_matrix[curr]:
                if x in cycle:
                    return False 
                if x not in visited:
                    if not topo(x, cycle.copy()):
                        return False 
                
            path.appendleft(curr)
            return True 
        
        for x in range(numCourses):
            if x not in visited:
                if topo(x, set()) == False:
                    return []
        
        return list(path)