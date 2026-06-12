class Solution {
    public int[] getConcatenation(int[] nums) {
        List<Integer> result = new ArrayList<Integer>();
        int k = 0;
        int n = nums.length;
        for(int i=0; i<=2*n - 1; i++){
            k = i % n;
            result.add(nums[k]);
        }
        int[] intArray = result.stream().mapToInt(Integer::intValue).toArray();
        return intArray;
    }
}