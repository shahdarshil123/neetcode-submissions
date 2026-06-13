class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] result = new int[2];

        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < numbers.length; i++){
            if(map.containsKey(numbers[i])){
                result = new int[]{map.getOrDefault(numbers[i],-1) + 1, i + 1};
                return result;
            }
            map.put(target - numbers[i], i);
        }

        return result;
    }
}
