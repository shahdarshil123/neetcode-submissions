class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # O(n^2) solution
        # sort the nums then iterate using loops
        nums.sort()
        n = len(nums)
        maxNumFreq = 1
        for i in range(n-1,-1,-1):
            count = 0
            t = k
            for j in range(i,-1,-1):
                if nums[i] - nums[j] > t:
                    break
                t = t - (nums[i] - nums[j])
                count += 1
            maxNumFreq = max(maxNumFreq, count)
        
        return maxNumFreq
            
                
