class Solution {
    public int countElements(int[] arr) {
        Set<Integer> numSet = new HashSet<Integer>();
        for(int num: arr){
            numSet.add(num);
        }
        int result = 0;
        for(int i=0; i<arr.length; i++){
            if(numSet.contains(arr[i]+1)){
                result++;
            }
        }
        return result;
    }
}
