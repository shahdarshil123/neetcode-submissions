class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)

        n = len(nums)
        prefix[0] = nums[0]
        suffix[n-1] = nums[n-1]

        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
            suffix[n-i-1] = suffix[n-i] + nums[n-i-1]
        
        score = -float('inf')
        for i in range(n):
            score = max(score,prefix[i], suffix[i])
        
        return score


            

