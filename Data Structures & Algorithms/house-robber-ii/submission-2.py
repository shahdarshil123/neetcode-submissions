class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        

        def helper(nums: List[int]):
            rob1 = 0
            rob2 = 0

            for i in range(len(nums)) :
                t = rob2
                rob2 = max(nums[i] + rob1, rob2)
                rob1 = t
            
            return rob2

        return max(helper(nums[0:-1]), helper(nums[1:]))