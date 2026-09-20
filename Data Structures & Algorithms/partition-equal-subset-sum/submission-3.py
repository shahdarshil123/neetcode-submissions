class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0 
        for num in nums:
            total += num
        
        if total % 2 != 0:
            return False
        
        # Try to make one subset half of the total
        cache = {}
        def dfs(i,add):   
            if add == total // 2:
                return True
            
            if i == len(nums):
                return False
            
            if (i,add) in cache:
                return cache[(i,add)]
            
            cache[(i,add)] = dfs(i+1,add + nums[i]) or dfs(i+1, add)
            return cache[(i,add)]
        
        return dfs(0,0)

        

