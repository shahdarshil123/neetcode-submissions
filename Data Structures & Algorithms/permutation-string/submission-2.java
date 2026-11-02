class Solution {
    public boolean checkInclusion(String s1, String s2) {
        // create a variable to track the characters in s1 and s2
        int[] s1Count = new int[26];
        int[] s2Count = new int[26];
        char chr;

        // iterate through s1
        for(int i=0; i < s1.length(); i++){
            chr = s1.charAt(i);
            s1Count[chr - 'a'] += 1;
        }
    
        // create a sliding window of length s1 and iterate through s2
        int left = 0;
        for(int right = 0; right < s2.length(); right++){
            s2Count[s2.charAt(right) - 'a'] += 1;
            if(right - left + 1 > s1.length()){
                s2Count[s2.charAt(left) - 'a'] -= 1;
                left++;
            }

            if(Arrays.equals(s1Count, s2Count)){
                return true;
            }
        }

        return false;
    }
}
