class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0 and abs(a) > abs(stack[-1]):
                stack.pop()
            if stack and stack[-1] > 0 and a < 0 and abs(a) == abs(stack[-1]):
                stack.pop()
            elif not stack or stack[-1] * a > 0 or (stack[-1] < 0 and a > 0) or (stack[-1] > 0 and a < 0 and abs(a) > abs(stack[-1])):
                stack.append(a)
        return stack 
                        