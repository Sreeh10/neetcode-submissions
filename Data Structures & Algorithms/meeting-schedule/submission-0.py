"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

def has_overlap(a,b):
    if ((a.end-a.start) + (b.end-b.start)) > (max(a.end,b.end) - min(a.start,b.start)):
        return True
    return False

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: (x.start, x.end))

        for i in range(1,len(intervals)):
            if has_overlap(intervals[i], intervals[i-1]):
                return False
        
        return True
