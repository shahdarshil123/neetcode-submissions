class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sMap = {}
        tMap = {}
        checkSet = set()
        minLength = float('inf')
        minString = ""

        for char in t:
            tMap[char] = tMap.get(char,0) + 1
        
        left = 0
        for right in range(len(s)):
            sMap[s[right]] = sMap.get(s[right],0) + 1
            if s[right] in tMap and sMap[s[right]] >= tMap[s[right]]:
                checkSet.add(s[right])
            while left <= right and len(checkSet) == len(tMap):
                # minLength = min(minLength, right-left+1)
                if right-left+1 < minLength:
                    minLength = right - left + 1
                    minString = s[left:right+1]

                sMap[s[left]] = sMap.get(s[left]) - 1
                if s[left] in tMap and sMap[s[left]] < tMap[s[left]]:
                    checkSet.remove(s[left])
                left += 1
        
        return minString
        
            
            
