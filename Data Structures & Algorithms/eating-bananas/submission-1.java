class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1;
        int right = 0;

        for(int pile: piles){
            right = Math.max(pile, right);
        }

        while(left < right){
            int mid = left + (right - left) / 2;
            if(countTime(mid, piles) > h){
                left = mid + 1;
            }
            else{
                right = mid;
            }
        }

        return left;
    }

    public long countTime(int rate, int[] piles){
        long time = 0;
        for(int pile: piles){
            time += (long) Math.ceil((double)pile/rate);
        }
        return time;
    }
    
}