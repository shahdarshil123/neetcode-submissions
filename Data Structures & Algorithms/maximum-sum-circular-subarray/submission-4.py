class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_val = float('inf')
        max_val = -float('inf')
        curr_sum = 0

        # find the total sum
        total = 0
        for i in range(len(nums)):
            total += nums[i]

        # Find the min_val
        for i in range(len(nums)):
            curr_sum += nums[i]
            min_val = min(min_val, curr_sum)
            if curr_sum > 0:
                curr_sum = 0
        
        # find the max_val
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            max_val = max(max_val, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
            
        if max_val < 0:
            return max_val
            
        return max(total - min_val, max_val)