class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1

        while left < right:
            while left < right and nums[left] % 2 == 0:
                left += 1
            while left < right and nums[right] % 2 != 0:
                right -= 1
            
            if left < right:
                t = nums[right]
                nums[right] = nums[left]
                nums[left] = t
                left += 1
                right -= 1
        
        return nums