class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] result = new int[2];
        int n = numbers.length;

        for(int i=0;i<=n-2;i++){
            int num1 = numbers[i];

            if(numbers[n-1] + num1 < target)
                continue;
            
            int left = i+1;
            int right = n - 1;
            int mid = 0;

            while(left <= right){
                mid = (left + right)/2;
                if(numbers[mid] + num1 == target){
                    result[0] = i+1;
                    result[1] = mid+1;
                    return result;
                }
                else if(numbers[mid] + num1 > target){
                    right = mid - 1;
                }
                else if(numbers[mid] + num1 < target){
                    left = mid + 1;
                }
            }

        }

        return result;
    }
}