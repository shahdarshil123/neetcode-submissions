class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;

        int maxArea = 0;
        int area;
        while(left < right){
            area = (Math.min(heights[left], heights[right]) * (right-left));
            if(maxArea < area){
                maxArea = area;
            }
            if(heights[left] <= heights[right]){
                left++;
            }
            else{
                right--;
            }
        }

        return maxArea;
    }
}
