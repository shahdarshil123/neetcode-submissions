class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        start = 0
        end = mountainArr.length() - 1

        # Find the peak element using Binary Search
        left = start
        right = end

        while left <= right:
            mid = left + (right - left) // 2
            mid_val = mountainArr.get(mid)
            mid_minus_1_val = mountainArr.get(mid - 1)
            mid_plus_1_val = mountainArr.get(mid + 1)

            peak_element = mid_val
            peak_element_indx = mid

            if mid_val > mid_minus_1_val and mid_val > mid_plus_1_val:
                break

            elif mid_minus_1_val < mid_val < mid_plus_1_val:
                left = mid + 1
            
            else:
                right = mid - 1
        
        print(peak_element_indx, peak_element)

        # Find the target value in the left side of the peak element
        left = start
        right = peak_element_indx

        while left <= right:
            mid = left + (right - left) // 2
            mid_val = mountainArr.get(mid)

            if mid_val == target:
                return mid
            
            elif mid_val < target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        # if not found on the left side search on the right of the peak element

        left = peak_element_indx + 1
        right = end

        while left <= right:
            mid = left + (right - left) // 2
            mid_val = mountainArr.get(mid)

            if mid_val == target:
                return mid
            
            elif mid_val > target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return -1
