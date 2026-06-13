class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Sliding window approch
        // Initialize the left right pointers
        int left = 0;

        int LS = 0;
        Set<Character> set = new HashSet<>();
        for(int right=0; right < s.length(); right++){
            while(set.contains(s.charAt(right))){
                set.remove(s.charAt(left));
                left++;
            }
            set.add(s.charAt(right));
            if(right - left + 1 > LS)
                LS = right - left + 1;
        }

        return LS;

    }
}
