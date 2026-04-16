class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = {i: [] for i in range(numRows)}
        iterator = []
        for i in range(numRows):
            iterator.append(i)
        for i in range(numRows-2,0,-1):
            iterator.append(i)

        n = len(iterator)

        for i in range(len(s)):
            row = iterator[i % n]
            rows[row].append(s[i])
        
        result = [] 
        for i in range(numRows):
            for c in rows[i]:
                result.append(c)
        
        return "".join(result)