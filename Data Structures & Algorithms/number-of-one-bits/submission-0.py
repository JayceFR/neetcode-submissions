class Solution:
    def hammingWeight(self, n: int) -> int:
        # is there a better way than converting to binary and then counting the number of 1s? 
        # we can keep right shifting 32 times and & 1 to get the sum 

        res = 0 
        for i in range(31):
            res += (n >> i) & 1 
        return res 
