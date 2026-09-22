"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []

        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        
        start.sort()
        end.sort()

        count = 0
        res = 0
        s = 0
        e = 0

        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)

        return res


