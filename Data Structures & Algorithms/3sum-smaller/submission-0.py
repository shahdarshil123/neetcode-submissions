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


        # Run outer loop for index i,j,k
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1, n):
                    val = nums[i] + nums[j] + nums[k]
                    if val >= target:
                        break
                    result += 1
        
        return result
            
                    
                
                

            
                
