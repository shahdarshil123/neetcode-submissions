class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> charMap = new HashMap<>();

        char maxChar;
        int maxCharCount = 0;
        int left = 0;
        int result = 0;
        for(int right = 0; right < s.length(); right++){
            charMap.put(s.charAt(right), charMap.getOrDefault(s.charAt(right),0)+1);
            if(charMap.get(s.charAt(right)) > maxCharCount){
                maxCharCount = charMap.get(s.charAt(right));
                maxChar = s.charAt(right);
            }
            while(left < right && ((right - left + 1) - maxCharCount) > k){
                // check if the char at left is max element or not
                charMap.put(s.charAt(left), charMap.get(s.charAt(left))-1);
                left++;
            }
            result = Math.max(result, right - left + 1);
        }

        return result;
    }
}



// "YYZA"