class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<Integer>();

        for(int ast: asteroids){
            while(!stack.isEmpty() && ast < 0 && stack.peek() > 0){
                int diff = ast + stack.peek();
                if(diff > 0){
                    ast = 0;
                }
                else if(diff < 0){
                    stack.pop();
                }
                else{
                    ast = 0;
                    stack.pop();
                }
            }
            if(ast != 0){
                stack.push(ast);
            }
        }

        return stack.stream().mapToInt(i->i).toArray();
    }
}