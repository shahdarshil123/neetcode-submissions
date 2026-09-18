class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Edge case:
        if len(words) == 1:
            return words[0]
            
        # create adjList of letters
        self.adjList = {}

        # write a function to create a dependency
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]

            if not self.helper(word1, word2):
                return ""
        
        # use topological graph to find the word
        result = []
        visit = set()
        path = set()
        
        def dfs(char):
            if char in visit:
                return True
            if char in path:
                return False
            path.add(char)
            for nei_char in self.adjList[char]:
                if not dfs(nei_char):
                    return False
            visit.add(char)
            result.append(char)
            path.remove(char)
            return True

        for char in self.adjList:
            if not dfs(char):
                return ""
        
        return "".join(result)

    
    def helper(self, word1, word2):
        # insert all the char in the self.adjList:
        for i in range(len(word1)):
            char1 = word1[i]
            if char1 not in self.adjList:
                self.adjList[char1] = []

        for i in range(len(word2)):
            char1 = word2[i]
            if char1 not in self.adjList:
                self.adjList[char1] = []

        for i in range(len(word1)):
            if i == len(word2):
                return False
            
            char1 = word1[i]
            char2 = word2[i]

            # if char1 not in self.adjList:
            #     self.adjList[char1] = []
            # if char2 not in self.adjList:
            #     self.adjList[char2] = []

            if char1 != char2:
                self.adjList[char2].append(char1)
                return True
        
        return True
            

            
