class Solution {
    public int longestConsecutive(int[] nums) {
        // create a set of integers
        Set<Integer> numSet = new HashSet<Integer>();

        // Add the numbers
        for(int num: nums){
            numSet.add(num);
        }

        // Iterate and check for the longest chain of numbers
        int longestConSeq = 0;
        int n, count=0;
        for(int num: nums){
            if(!numSet.contains(num-1)){
                n = num;
                count = 0;
                while(numSet.contains(n)){
                    count++;
                    n++;
                }
            }
            if(count > longestConSeq){
                longestConSeq = count;
            }
        }
        
        return longestConSeq;
    }
}
