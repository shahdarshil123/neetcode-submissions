class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        # Time complexity: O(n*m)
        numMap = {}
        for arr in arrays:
            for num in arr:
                numMap[num] = numMap.get(num,0) + 1

        result = []
        n = len(arrays)
        for num in arrays[0]:
            if numMap[num] == n:
                result.append(num)
        
        return result


