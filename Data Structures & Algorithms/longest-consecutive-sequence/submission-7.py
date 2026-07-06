class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        
        num_set = set(nums)
        LCS = 1
        for num in nums:
            if num - 1 not in num_set:
                n = num
                count = 0
                while n in num_set:
                    count += 1
                    n += 1
                LCS = max(LCS, count)
        
        return LCS
        
        
