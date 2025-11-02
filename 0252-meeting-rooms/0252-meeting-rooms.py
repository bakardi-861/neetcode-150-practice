class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        last = float("-inf")
        for s,e in intervals:
            if last > s:
                return False
            else:
                last = e
        return True