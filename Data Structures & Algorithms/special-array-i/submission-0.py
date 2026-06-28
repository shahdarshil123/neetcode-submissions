class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev = nums[0] % 2
        for i in range(1,len(nums)):
            if (nums[i] % 2 == 0 and prev == 0) or (nums[i] % 2 == 1 and prev == 1):
                return False
            prev = nums[i] % 2
        return True