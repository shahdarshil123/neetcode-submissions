class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        nums.sort()
        LCS = 1
        curr = 1
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] > 1:
                curr = 1
            elif nums[i] - nums[i-1] == 0:
                continue
            else:
                curr += 1
                LCS = max(LCS, curr)
        
        return LCS