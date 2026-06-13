class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        Stack<Integer> stack = new Stack<Integer>();
        int[] result = new int[n];
        
        for(int i = 0; i < n; i++){
            while(!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]){
                int j = stack.pop();
                result[j] = i - j;
            }
            stack.push(i);
        }

        return result;
    }
}
