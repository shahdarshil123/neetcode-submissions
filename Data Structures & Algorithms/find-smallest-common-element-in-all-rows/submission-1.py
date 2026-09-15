class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        rows, columns = len(mat), len(mat[0])
        if rows == 1:
            return mat[0][0]

        for num in mat[0]:
            count = 0
            for r in range(1,rows):
                if not self.binary_search(mat[r], num):
                    break
                count += 1
            if count == rows - 1:
                return num
        return -1
                
    def binary_search(self, arr, num):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == num:
                return True
            elif arr[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

                


