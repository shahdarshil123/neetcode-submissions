class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String word: strs){
            sb.append(Integer.toString(word.length()));
            sb.append('#');
            sb.append(word);
        }
        String encodedString = sb.toString();
        return encodedString;
    }

    public List<String> decode(String str) {
        List<String> wordList = new ArrayList<>();
        int i = 0;
        StringBuilder sb = new StringBuilder();
        while(i < str.length()){
            int num = 0;
            // find the length of the word string
            while(i < str.length() && Character.isDigit(str.charAt(i))){
                num = num*10 + (str.charAt(i) - '0');
                i++;
            }
            // skip delimiter '#'
            if(i < str.length() && str.charAt(i) == '#'){
                i++;
            }
            // create the string and add it to the string builder
            for(int j = 0; j < num; j++){
                sb.append(str.charAt(i));
                i++;
            }
            wordList.add(sb.toString());
            sb.setLength(0);
        }
        return wordList;
    }
}