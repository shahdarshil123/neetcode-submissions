class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = [intervals[0]]

        for i in range(1,len(intervals)):
            start, end = intervals[i]
            prev_start, prev_end = result[-1]

            if prev_start <= start <= prev_end:
                result.pop()
                result.append([prev_start, max(prev_end, end)])
            
            else:
                result.append([start, end])

        return result