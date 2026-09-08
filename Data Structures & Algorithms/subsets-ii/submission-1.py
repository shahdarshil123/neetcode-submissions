class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        result = []

        def dfs(i):
            if i == len(nums):
                result.append(arr.copy())
                return
            
            arr.append(nums[i])
            dfs(i+1)
            arr.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)
        
        dfs(0)
        return result
            
            

