class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        arr = []

        def backtracking(i):
            if i == len(nums):
                result.append(arr.copy())
                return
            
            arr.append(nums[i])
            backtracking(i+1)

            arr.pop()
            backtracking(i+1)
        
        backtracking(0)
        return result
            
            