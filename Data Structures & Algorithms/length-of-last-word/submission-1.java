class Solution {
    public int lengthOfLastWord(String s) {
        int wordLength = 0;
        int lastWordLength = 0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i) != ' '){
                wordLength += 1;
            }
            else{
                if(wordLength != 0){
                    lastWordLength = wordLength;
                }
                wordLength = 0;
            }
        }
        if(wordLength != 0){
            lastWordLength = wordLength;
        }
        return lastWordLength;
    }
}