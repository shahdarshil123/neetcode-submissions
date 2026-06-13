class Solution {
    public int maxArea(int[] heights) {
        int n = heights.length;
        int area;
        int maxArea = 0;

        for(int i = 0; i < n-1; i++){
            for(int j = i+1; j < n; j++){
                area = (j - i)*Math.min(heights[i], heights[j]);
                if(area > maxArea){
                    maxArea = area;
                }
            }
        }

        return maxArea;
    }
}
