class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Odd length
        result = ""
        count = 0
        for i in range(len(s)):
            left, right = i, i
            while left-1 >= 0 and right+1 < len(s) and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            if right - left + 1 > count:
                count = right - left + 1
                result = s[left:right+1]
    
        # even length
        for i in range(len(s)-1):
            left, right = i, i+1
            if s[left] != s[right]:
                continue
            while left-1 >= 0 and right+1 < len(s) and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            if right - left + 1 > count:
                count = right - left + 1
                result = s[left:right+1]
        
        return result