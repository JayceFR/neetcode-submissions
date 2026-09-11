class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        square = [0, 0, 0, 0] # T R B L 

        permiter = sum(matchsticks)
        if (permiter // 4) * 4 != permiter:
            return False 

        size = permiter // 4 

        matchsticks.sort(reverse=True)

        print("size", size)
        def isValidSq(square):
            for s in square:
                if s != size:
                    return False  
            return True 

        def backtrack(pos: int, square: List[int]) -> bool:
            if pos == len(matchsticks):
                return isValidSq(square)
            m = matchsticks[pos]
            for p in range(len(square)):
                if square[p] + m <= size:
                    # add it to that side
                    square[p] += m 
                    if backtrack(pos + 1, square):
                        return True 
                    square[p] -= m 
            
            return False 

        return backtrack(0, square)