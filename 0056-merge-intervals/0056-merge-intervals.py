class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        merged = []
        j = 1
        for i in intervals:
            # nothing merged or last merged end < current start
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else: # merge: change the last end time to the max of last merged or current (smaller start time is kept)
                merged[-1][1] = max(merged[-1][1],i[1])
        return merged