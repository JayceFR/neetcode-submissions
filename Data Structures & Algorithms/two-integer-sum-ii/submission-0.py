class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        its sorted so its a 2 pointer question 
        1,2,3,5, target = 5 
        fp = 1
        rp = 2 
        6 > 5:
            rp -- 
        4 < 5:
            fp ++ 
        5 == 5:
            boom 
        '''
        fp = 0
        rp = len(numbers) - 1
        while fp < rp:
            if numbers[fp] + numbers[rp] > target:
                rp -= 1 
            elif numbers[fp] + numbers[rp] < target:
                fp += 1 
            else:
                return [fp + 1, rp + 1]