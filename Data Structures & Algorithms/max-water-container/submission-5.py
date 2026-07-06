class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_vol = 0

        while left < right:
            vol = min(heights[left], heights[right]) * (right-left)
            max_vol = max(vol, max_vol)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_vol
            