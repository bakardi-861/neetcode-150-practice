class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # if i would have to merge an interval bc start = start, delete the one I would merge
        # end == start is ok
        intervals.sort(key=lambda x: x[1]) # this only seems to work when sorted by end time
        last = float("-inf")
        count = 0
        for s,e in intervals:
            if last <= s:
                last = e
            else:
                count += 1
        return count