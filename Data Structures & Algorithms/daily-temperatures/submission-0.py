class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for x in range(len(temperatures))]

        stack = []
        for pos, t in enumerate(temperatures): 
            while stack and t > stack[-1][0]:
                n, i = stack.pop()
                result[i] = pos - i 
            stack.append((t,pos))
        return result
            
