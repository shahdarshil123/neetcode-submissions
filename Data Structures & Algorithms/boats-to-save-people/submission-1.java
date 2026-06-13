class Solution {
    public int numRescueBoats(int[] people, int limit) {
        int boats = 0;
        Arrays.sort(people);
        // System.out.println(Arrays.toString(people));

        int left = 0;
        int right = people.length - 1;

        while(left < right){
            if(people[left] + people[right] <= limit){
                left++;
                right--;
            }
            else{
                right--;
            }
            boats += 1;
        }
        if(left == right)
            boats+=1;
        return boats;
    }
}