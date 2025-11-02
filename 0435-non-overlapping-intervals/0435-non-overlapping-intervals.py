class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # if i would have to merge an interval bc start = start, delete the one I would merge
        # end == start is ok
        intervals.sort(key=lambda x: x[1])
        merged = []
        count = 0
        for s,e in intervals:
            if not merged or merged[-1][1] <= s:
                merged.append([s,e])
            else:
                count += 1
        return count