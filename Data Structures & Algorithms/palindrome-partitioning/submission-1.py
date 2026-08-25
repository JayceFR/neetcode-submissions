class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sols = []

        def dfs(sol, pos):
            if pos == len(s):
                pal = True 
                for so in sol:
                    if so != so[::-1]:
                        pal = False 
                if pal:
                    sols.append(sol.copy())
                return 

            sol.append(s[pos])
            dfs(sol, pos+1) #no check needed 
            
            # print("before adding to the left", sol)
            sol.pop()
            sol[-1] = sol[-1] + s[pos]
            # if sol[-1] == sol[-1][::-1]:
            dfs(sol, pos+1)

        dfs([s[0]], 1)
        
        return sols 


            