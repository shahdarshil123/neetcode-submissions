class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {}
        max_f = 0
        left = 0
        result = 0
        for right in range(len(s)):
            char_map[s[right]] = char_map.get(s[right], 0) + 1
            max_f = max(max_f, char_map[s[right]])
            while right - left + 1 - max_f > k:
                char_map[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        
        return result