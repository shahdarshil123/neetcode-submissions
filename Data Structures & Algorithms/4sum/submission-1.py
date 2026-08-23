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
                for c in range(b+1, len(nums)-1):
                    if c-1 > b and nums[c] == nums[c-1]:
                        continue
                    for d in range(c+1, len(nums)):
                        if d-1 > c and nums[d] == nums[d-1]:
                            continue
                        if nums[a] + nums[b] + nums[c] + nums[d] == target:
                            result.append([nums[a], nums[b], nums[c], nums[d]])
        
        return result