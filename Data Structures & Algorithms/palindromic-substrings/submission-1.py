class Solution:
    def countSubstrings(self, s: str) -> int:
        # Odd count
        count = 0
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                count += 1
                left -= 1
                right += 1
                
        
        # Even count
        for i in range(len(s)-1):
            left, right = i, i+1
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                count += 1
                left -= 1
                right += 1
        
        return count