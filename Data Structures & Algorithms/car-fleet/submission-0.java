class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        List<int[]> arrList = new ArrayList<int[]>();
        for(int i=0; i<position.length;i++){
            int[] a = new int[]{position[i], speed[i]};
            arrList.add(a);
        }
        arrList.sort((a,b)->b[0] - a[0]);

        Stack<Double> stack = new Stack<Double>();
        for(int i=0; i < arrList.size(); i++){
            double time = (double)(target - arrList.get(i)[0]) / arrList.get(i)[1];
            if(stack.isEmpty() || time > stack.peek()){
                stack.push(time);
            }
        }

        return stack.size();
    }
}
