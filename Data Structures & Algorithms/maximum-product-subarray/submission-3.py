class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP, minP = 1, 1
        res = nums[0]
        for num in nums:
            if num == 0:
                maxP, minP = 1, 1
                res = max(res, 0)
                continue
            t = maxP
            maxP = max(num, num*maxP, num*minP)
            minP = min(num, num*t, num*minP)
            res = max(res, maxP, minP)
        
        return res