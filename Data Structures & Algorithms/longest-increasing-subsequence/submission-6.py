class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = 1
        dp = [1]*(len(nums))
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
            LIS = max(LIS, dp[i])
        return LIS
                
    