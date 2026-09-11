class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        count = 0
        curr_prod = 1
        left = 0
        for right in range(len(nums)):
            curr_prod = curr_prod * nums[right]
            while curr_prod >= k:
                curr_prod = curr_prod // nums[left]
                left += 1
            count += (right - left + 1)
        return count
