class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for s,e in intervals:
            if not merged or merged[-1][1] <= s:
                merged.append([s,e])
            else:
                merged[-1][1] = max(e,merged[-1][1])
        return len(merged) == len(intervals)