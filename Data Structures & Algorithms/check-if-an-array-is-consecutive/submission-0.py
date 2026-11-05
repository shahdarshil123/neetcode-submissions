class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        # check the smallest element in the array
        smallest = nums[0]
        numSet = set()
        for num in nums:
            if smallest > num:
                smallest = num
            numSet.add(num)
        
        n = len(nums)
        for num in range(smallest, smallest+n):
            if num not in numSet:
                return False
        
        return True