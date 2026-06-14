class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // Define variables below:
        int rows = matrix.length;
        int columns = matrix[0].length;

        //First find the correct row using binary search
        int top = 0;
        int bottom = rows - 1;
        int mid = 0;

        while(top <= bottom){
            mid = (top + bottom) / 2;
            if(matrix[mid][0] <= target && matrix[mid][columns-1] >= target)
                break;
            else if(matrix[mid][0] < target)
                top = mid + 1;
            else
                bottom = mid - 1;
        }

        int row = mid;
        System.out.println("Search row is "+ row);
        //Search within the correct column using binary search

        int left = 0;
        int right = columns - 1;

        while(left <= right){
            mid = (left + right) / 2;
            if(matrix[row][mid] == target)
                return true;
            else if(matrix[row][mid] > target)
                right = mid - 1;
            else
                left = mid + 1;
        }


        return false;
    }
}
