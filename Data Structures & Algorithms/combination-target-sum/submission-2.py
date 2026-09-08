class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        arr = []

        def backtracking(i, total):
            if i == len(nums):
                if total == target:
                    result.append(arr.copy())
                return
            
            if total > target:
                return
            
            arr.append(nums[i])
            backtracking(i, total+nums[i])

            arr.pop()
            backtracking(i+1, total)
        
        backtracking(0,0)
        return result

