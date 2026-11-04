class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFreq = 1
        total = 0
        left = 0
        for right in range(len(nums)):
            total += nums[right]
            while left < right and nums[right]*(right-left+1) > total + k:
                total -= nums[left]
                left += 1
            maxFreq = max(maxFreq, right-left+1)
        
        return maxFreq
            
            
                
