class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        arr = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            prev_start, prev_end = arr[-1][0], arr[-1][1]

            if prev_start <= start < prev_end:
                if end < prev_end:
                    arr.pop()
                    arr.append(intervals[i])
            else:
                arr.append(intervals[i])
        
        return len(intervals) - len(arr)