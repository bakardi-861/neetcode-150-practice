class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        new_start, new_end = newInterval
        for curr_start, curr_end in intervals:
            # if new end before curr_start, just append it and append the rest of intervals after
            if new_end < curr_start:
                res.append([new_start, new_end])
                res += intervals[intervals.index([curr_start, curr_end]):]
                return res
            # append everything before the newInterval
            elif new_start > curr_end:
                res.append([curr_start, curr_end])
            # merge: set new curr_start and curr_end as the min and max of both
            # keep comparing new to current
            else:
                new_start = min(new_start, curr_start)
                new_end = max(new_end, curr_end)
        # insert new interval
        res.append([new_start, new_end])
        return res