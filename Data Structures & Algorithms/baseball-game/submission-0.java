class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<Integer>();

        for(String ops: operations){
            if(ops.equals("+")){
                int num1 = stack.pop();
                int num2 = stack.peek();

                stack.push(num1);
                stack.push(num1 + num2);
            }
            else if(ops.equals("C")){
                stack.pop();
            }
            else if(ops.equals("D")){
                int doub = 2*stack.peek();
                stack.push(doub);
            }
            else{
                stack.push(Integer.parseInt(ops));
            }
            }

        int score = 0;
        for(int sc: stack){
            score += sc;
        }

        return score;
    }
}