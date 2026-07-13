class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Optimized solution
        nums_map = {}
        result = []
        for i in range(len(nums)):
            if target - nums[i] in nums_map:
                result.append(nums_map[target-nums[i]])
                result.append(i)
                return result
            nums_map[nums[i]] = i
        return result
        