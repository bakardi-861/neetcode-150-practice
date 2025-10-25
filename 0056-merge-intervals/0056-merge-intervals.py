class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # write pseudocode, then change to correct code
        merged = []
        intervals.sort(key=lambda x:x[0])

        for interval in intervals:
            # if merged array is empty or last merged end time is smaller than current interval start time
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else: # current interval is smaller than last merged, so that means we have to merge both
                # merge current interval into last merged interval
                merged[-1] = [min(interval[0],merged[-1][0]),max(interval[1],merged[-1][1])]
        return merged