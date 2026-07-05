class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        answer = []

        prod = 1
        for i in range(len(nums)-1):
            prod = prod*nums[i]
            left.append(prod)
        
        prod = 1
        for i in range(len(nums)-1,0,-1):
            prod = prod*nums[i]
            right.append(prod)
        right.reverse()

        for i in range(len(left)):
            answer.append(left[i] * right[i])
        
        return answer

