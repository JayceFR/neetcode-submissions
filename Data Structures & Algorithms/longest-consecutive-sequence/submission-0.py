class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_count = 0 
        count = 0 
        for num in nums:
            count = 0
            if (num - 1) not in numset:
                dup_num = num
                while dup_num in numset: 
                    count += 1
                    dup_num += 1
                if count > max_count:
                    max_count = count
        return max_count 


        