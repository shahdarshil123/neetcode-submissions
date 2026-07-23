class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        maxf = 0
        left = 0
        res = 0
        for right in range(len(s)):
            charMap[s[right]] = charMap.get(s[right], 0) + 1
            maxf = max(maxf, charMap[s[right]])

            while right - left + 1 - maxf > k:
                charMap[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        
        return res