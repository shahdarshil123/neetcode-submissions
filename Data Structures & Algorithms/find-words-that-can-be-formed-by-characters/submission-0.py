class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_map = {}
        for char in chars:
            char_map[char] = char_map.get(char,0) + 1
        
        result = 0
        for word in words:
            t = {}
            flag = True
            for char in word:
                if char not in char_map:
                    flag = False
                    break
                t[char] = t.get(char,0) + 1
                if t[char] > char_map[char]:
                    flag = False
                    break
            if flag:
                result += len(word)
        
        return result

