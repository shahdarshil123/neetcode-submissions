class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        s = set()
        result = []

        def dfs():
            if len(arr) >= len(nums):
                result.append(arr.copy())
                return
            
            for i in range(len(nums)):
                if i not in s:
                    arr.append(nums[i])
                    s.add(i)
                    dfs()
                    s.remove(i)
                    arr.pop()
            
        dfs()
        return result
            

            








