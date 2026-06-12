class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<Integer>();
        for(int num: nums){
            numSet.add(num);
        }

        int res = 0;
        for(int num: nums){
            int n = num;
            int count = 0;
            while(numSet.contains(n)){
                count++;
                n++;
            }
            if(count > res){
                res = count;
            }
        }

        return res;
    }
}
