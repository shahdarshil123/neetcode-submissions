class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        charMap = {}
        result = 0
        for char in s:
            charMap[char] = charMap.get(char,0) + 1
            result += charMap[char]
        
        return result