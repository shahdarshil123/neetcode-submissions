class Solution {
    public int maxProfit(int[] prices) {
        int buy = Integer.MAX_VALUE;
        int profit = 0;
        int maxProfit = 0;

        for(int i = 0; i < prices.length; i++){
            if(prices[i] < buy){
                buy = prices[i];
                continue;
            }
            profit = prices[i] - buy;
            if(profit > maxProfit){
                maxProfit = profit;
            }
        }
        return maxProfit;
    }
}
