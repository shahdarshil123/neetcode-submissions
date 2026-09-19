class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def dfs(i):
            if i == len(s):
                return True
            
            if i > len(s):
                return False
            
            if i in cache:
                return cache[i]

            cache[i] = False    
            for word in wordDict:
                n = len(word)
                if s[i:i+n] == word:
                    if dfs(i+n):
                        cache[i] = True
                        return True
            return False
        
        return dfs(0)

                