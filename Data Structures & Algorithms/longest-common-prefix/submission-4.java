class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 1){
            return strs[0];
        }
        Arrays.sort(strs);

        int L = strs.length - 1;
        for(int i = 0; i < strs[0].length(); i++){
            if(strs[0].charAt(i) != strs[L].charAt(i)){
                return strs[0].substring(0,i);
            }
        }

        return strs[0];
    }
}