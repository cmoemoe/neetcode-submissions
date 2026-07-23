"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #order start times
        # [(0,30),(5,10),(15,20)]
        # start = 5
        # end = 30
        # 30 > 5 -> False 

        if len(intervals) == 0 or len(intervals) == 1:
            return True
        
        intervals.sort(key = lambda i: i.start)
        
        for i in range(1, len(intervals)):
            start = intervals[i].start
            end = intervals[i-1].end

            if end > start:
                return False
        
        return True

    

