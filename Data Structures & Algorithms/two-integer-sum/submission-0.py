class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        ans = []
        for i in range(len(nums)):
            if(nums[i] in map.keys()):
                ans.append(map[nums[i]])
                ans.append(i)
            else:
                map[target-nums[i]] = i
        return ans