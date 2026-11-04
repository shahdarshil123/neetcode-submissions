class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # Edge cases
        if len(nums) < 3:
            return 0

        # Variables
        result = 0
        n = len(nums)

        # sort the elements
        nums.sort()

        # Run outer loop for index i
        for i in range(n-2):
            left = i + 1
            right = n - 1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val < target:
                    result += right - left
                    left += 1
                else:
                    right -= 1
        
        return result