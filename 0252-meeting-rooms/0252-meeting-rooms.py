class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0]
        for i in range(1,len(intervals)):
            start,end = intervals[i]
            if start < prev[1]:
                return False
            prev = [start,end]
        return True

# [[2,4],[7,10]]
#             i