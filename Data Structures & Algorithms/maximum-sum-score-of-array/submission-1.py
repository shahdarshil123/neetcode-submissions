class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        total = sum(nums)
        score = -float('inf')
        prefix = 0

        for num in nums:
            score = max(score, total-prefix)
            prefix += num
            score = max(score, prefix)
        
        return score
        


            

