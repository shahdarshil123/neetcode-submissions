class Solution {
    public int largestUniqueNumber(int[] nums) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i=0; i<nums.length; i++){
            map.put(nums[i], map.getOrDefault(nums[i],0) + 1);
        }

        int result = -1;
        for(int num: map.keySet()){
            if(map.get(num) == 1 && num > result){
                result = num;
            }
        }
        return result;
    }
}
