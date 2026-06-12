class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
       Map<Character, Integer> sCount = new HashMap<Character, Integer>();
       Map<Character, Integer> tCount = new HashMap<Character, Integer>();

       for(int i=0; i<s.length(); i++){
            sCount.put(s.charAt(i), sCount.getOrDefault(s.charAt(i), 0)+1);
            tCount.put(t.charAt(i), tCount.getOrDefault(t.charAt(i), 0)+1);
       }

       return sCount.equals(tCount);
    }
}
