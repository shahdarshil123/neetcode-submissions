class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // maintain a anagram map of each word
        Map<String, List<String>> groupMap = new HashMap<>();

        // find the sorted string for each word and add it to the map
        for(String word: strs){
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String key = new String(charArray);

            // if(!groupMap.containsKey(key)){
            //     groupMap.put(key, new ArrayList<String>());
            // }
            // groupMap.get(key).add(word);
            groupMap.computeIfAbsent(key, k -> new ArrayList<String>()).add(word);
        }

        // take each group and add to array list
        List<List<String>> result = new ArrayList<>();
        
        for(Map.Entry<String, List<String>> entry: groupMap.entrySet()){
            result.add(entry.getValue());
        }

        // return the list
        return result;
    }
}
