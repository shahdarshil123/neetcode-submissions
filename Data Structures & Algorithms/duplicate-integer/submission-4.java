class Solution {
    public boolean hasDuplicate(int[] nums) {
        // create a set and assign values to the set
        Set<Integer> set = new HashSet<>();

        for(int num: nums){
            if(!set.add(num)){
                return true;
            }
        }
        
        return false;
    }
}