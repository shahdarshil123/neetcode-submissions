class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int columns = matrix[0].length;

        // Find the appropriate row using binary search
        int top = 0;
        int bottom = rows - 1;
        int mid = 0;

        // find the row
        while (top <= bottom) {
            mid = top + (bottom - top) / 2;
            if (matrix[mid][0] <= target && matrix[mid][columns - 1] >= target) {
                break;
            }
            if (matrix[mid][0] > target) {
                bottom = mid - 1;
            } else if (matrix[mid][columns - 1] < target) {
                top = mid + 1;
            }
        }

        if (top > bottom) {
            return false;
        }
        
        int row = mid;

        // find the column with that row
        int left = 0;
        int right = columns - 1;

        while (left <= right) {
            mid = left + (right - left) / 2;
            if (matrix[row][mid] == target) {
                return true;
            } else if (matrix[row][mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return false;
    }
}