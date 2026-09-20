class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0 
        for num in nums:
            total += num
        
        if total % 2 != 0:
            return False
        
        # Try to make one subset half of the total
        
        def dfs(i,add):   
            if add == total // 2:
                return True
            
            if i == len(nums):
                return False
            
            return dfs(i+1,add + nums[i]) or dfs(i+1, add)
        
        return dfs(0,0)

        

