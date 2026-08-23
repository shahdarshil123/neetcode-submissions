class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        
        for a in range(len(nums)-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1,len(nums)-2):
                if b-1 > a and nums[b] == nums[b-1]:
                    continue

                c = b+1
                d = len(nums) - 1

                while c < d:
                    current_sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if current_sum == target:
                        result.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c] == nums[c+1]:
                            c += 1
                        while c < d and nums[d] == nums[d-1]:
                            d -= 1
                        c += 1
                        d -= 1
                    
                    elif current_sum < target:
                        c += 1
                    
                    else:
                        d -= 1
        
        return result