class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Using binary search
        result = [0,0]
        for i in range(len(numbers)-1):
            left = i + 1
            right = len(numbers)-1
            while left <= right:
                mid = (left + right) // 2
                if numbers[i] + numbers[mid] == target:
                    result[0] = i+1
                    result[1] = mid+1
                    return result
                elif numbers[i] + numbers[mid] < target:
                    left = mid + 1
                elif numbers[i] + numbers[mid] > target:
                    right = mid - 1
        
        return result


