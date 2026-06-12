class Solution {
    public String longestCommonPrefix(String[] strs) {
     if(strs.length == 0){return "";}
     // Find the smallest word from the list
     String minStr = strs[0];
     int n = strs[0].length();

     for(String s: strs){
        if(s.length() < n){
            minStr = s;
            n = s.length();
        }
     }

     // Iterate in the list to find the longest prefix
     String result = "";
     for(int i=0; i < n; i++){
        for(int j=0; j < strs.length; j++ ){
            if(strs[j].charAt(i) != strs[0].charAt(i))
                return result;
        }
        result += strs[0].charAt(i);
     }

     return result;
    }
}