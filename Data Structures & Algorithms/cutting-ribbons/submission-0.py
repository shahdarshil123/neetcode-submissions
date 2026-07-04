class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        total_length = 0
        for ribbon in ribbons:
            total_length += ribbon
        
        if total_length < k:
            return 0
            
        n = total_length // k

        def is_possible(n):
            if n == 0: return True
            total_ribbons = 0
            for ribbon in ribbons:
                total_ribbons += ribbon // n
            if total_ribbons >= k:
                return True
            return False

        left = 1
        right = n
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans