class Solution {
    public long numberOfSubstrings(String s) {
        long result = 0;
        Map<Character, Integer> charMap = new HashMap<>();
        for(char chr: s.toCharArray()){
            charMap.put(chr, charMap.getOrDefault(chr,0)+1);
            result += charMap.get(chr);
        }
        return result;
    }
}
