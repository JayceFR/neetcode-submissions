class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        '''
        For a 5 we return nothing 
        For a 10 we return 5
        For a 20 we can return either 5,5,5 or 10,5
        '''
        reg = [0,0,0] # 5, 10, 20

        m = {5:0, 10:1, 20:2}

        for bill in bills:
            reg[m[bill]] += 1 

            if bill == 10:
                if reg[0] == 0:
                    return False 
                reg[0] -= 1 
            elif bill == 20:
                # be greedy and give out the 10 note first 
                if reg[1] >= 1 and reg[0] >= 1:
                    reg[1] -= 1 
                    reg[0] -= 1 
                elif reg[0] >= 3: # give 5 if there is no option 
                    reg[0] -= 3
                else:
                    return False 
        return True 
