class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // Variables
        List<List<Integer>> result = new ArrayList<>();
        //Sort the array first
        Arrays.sort(nums);

        // use the outer for loop
        for(int i=0; i < nums.length-2; i++){
            if(i > 0 && nums[i] == nums[i-1])
                continue;

            // Run the two pointers
            int j = i+1;
            int k = nums.length-1;
            int target;

            while(j < k){
                target = nums[i] + nums[j] + nums[k];
                if(target == 0){
                    result.add(new ArrayList<Integer>(Arrays.asList(nums[i], nums[j], nums[k])));
                    while(j < k && nums[j] == nums[j+1]) j++;
                    while(j < k && nums[k] == nums[k-1]) k--;
                    j++;
                    k--;
                }
                else if(target < 0){
                    j++;
                }
                else{
                    k--;
                }
            }
        }

        return result;

    }
}
