class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;

        if(n == 1){
            return 1;
        }

        int left = 1;
        int right = 1;
        
        while(right < n){
            while(right < n && nums[right-1] == nums[right]){
                right++;
            }

            if(right < n){
            nums[left] = nums[right];
            }
            else{
                return left;
            }

            left++;
            right++;
        }

        return left;

    }
}