class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # backtracking soluiton with bfs to find the minimum length 
        q = deque()
        q.append(("0000", 0)) # (start, level)
        deads = set(deadends)

        if "0000" in deads:
            return -1 

        visited = set()
        while q:
            curr, level = q.popleft()
            if curr not in visited:
                if curr == target:
                    return level # found 
                visited.add(curr)
                # consider the 8 possibilities 
                for x in range(4):
                    for delta in [-1, 1]:
                        wheel = (int(curr[x]) + delta) % 10 
                        lock = curr[:x] + str(wheel) + curr[x+1:]
                        if lock not in visited and lock not in deads:
                            q.append((lock, level + 1))
        
        return -1 

