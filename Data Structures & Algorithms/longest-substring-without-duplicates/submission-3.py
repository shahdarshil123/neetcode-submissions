class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        result = 0
        count = 0
        for right in range(len(s)):
            while left < right and s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                count -= 1
            char_set.add(s[right])
            count += 1
            result = max(result, count)
        return result
            
