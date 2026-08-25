class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort time boyysss

        def msort(nums):
            n = len(nums)

            # base case 
            if n == 1: 
                return nums 

            # split in half 
            lnums = nums[0:n//2]
            rnums = nums[n//2:n]

            # recurs
            lhalf = msort(lnums)
            rhalf = msort(rnums)

            # merge them 
            ns = []
            lp = 0 
            rp = 0 
            while lp < len(lhalf) and rp < len(rhalf):
                if lhalf[lp] < rhalf[rp]:
                    ns.append(lhalf[lp])
                    lp += 1 
                else:
                    ns.append(rhalf[rp])
                    rp += 1 
            
            if lp == len(lhalf):
                ns += rhalf[rp:len(rhalf)]
            else:
                ns += lhalf[lp:len(lhalf)]

            return ns 
        
        return msort(nums)