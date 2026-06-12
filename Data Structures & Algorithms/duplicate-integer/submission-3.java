class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> hashSet = new HashSet<Integer>();

        for(int num: nums){
            if(hashSet.contains(num))
                return true;
            hashSet.add(num);
        }

        return false;
    }
}