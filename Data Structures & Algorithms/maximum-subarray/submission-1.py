class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum_sum = nums[0]
        curr_sum = 0
        for num in nums:
            curr_sum += num
            maximum_sum = max(maximum_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        
        return maximum_sum
        
