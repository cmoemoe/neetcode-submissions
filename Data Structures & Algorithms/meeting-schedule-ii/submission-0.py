"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#use a heap and keep max 
#conider ends before starts 

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        max_res = 0
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s, e = 0,0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            max_res = max(max_res, count)

        return max_res



        

