class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Define variables below:
        Map<Integer, Integer> map1 = new HashMap<Integer, Integer>();
        List<int[]> arrList = new ArrayList<int[]>();

        // Find the freq of each number
        for(int num: nums){
            map1.put(num, map1.getOrDefault(num, 0)+1);
        }
        
        // Create an arr of number, freq and sort it desc
        for(Map.Entry<Integer, Integer> entry: map1.entrySet()){
            int[] arr = new int[]{entry.getValue(), entry.getKey()};
            arrList.add(arr);
        }

        //Sort the arrList with freq, num in desc order
        arrList.sort((a,b) -> b[0] - a[0]);

        // Find the k freq elements
        int[] res = new int[k];
        for(int i=0; i < k; i++){
            res[i] = arrList.get(i)[1];
        }

        return res;

    }
}
