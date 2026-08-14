class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        leftMaxArr = [height[0]]
        for j in range(1,len(height)):
            leftMaxArr.append(max(leftMaxArr[-1], height[j]))
        
        rightMaxArr = [height[-1]]
        for j in range(len(height)-2,-1,-1):
            rightMaxArr.append(max(rightMaxArr[-1], height[j]))
        rightMaxArr.reverse()
        
        for i in range(len(height)):
            result += min(rightMaxArr[i], leftMaxArr[i]) - height[i]
        return result