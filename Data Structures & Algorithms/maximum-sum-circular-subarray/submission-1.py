class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # maxSum = nums[0]
        # currSum = 0
        # cs, ce = 0, 0 
        # ms, me = 0, 0 
        # for i, val in enumerate(nums):
        #     currSum += val
        #     if currSum > maxSum:
        #         maxSum = currSum
        #         ms, me = cs, i 
        #     if currSum < 0:
        #         currSum = 0 
        #         # reset the current pointers
        #         cs = i + 1 
        #         ce = i + 1
        #     else:
        #         # update the end pointer 
        #         ce = i 

        # print(ms, me, maxSum)
        # if me == len(nums) - 1:
        #     # We have included the last item, must try to grow the sub array upto ms 
        #     tmpSum = maxSum
        #     for i in range(0, ms):
        #         tmpSum += nums[i]
        #         maxSum = max(maxSum, tmpSum)

        # Initially thought of using Kadane, and then if the subarray includes the last element, extend it. 
        # But that breaks for the input [5, -3, 5] were the max is 10, while ours would reutrn 7 
        # intended solution is soo smart!

        globMax, globMin = nums[0], nums[0]

        currMax, currMin = 0, 0
        total = 0 

        for num in nums:
            currMax = max(currMax + num, num)
            currMin = min(currMin + num, num)
            total += num 
            globMax = max(globMax, currMax)
            globMin = min(globMin, currMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax 