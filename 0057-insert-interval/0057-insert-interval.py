class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # naive way to do this is to insert new interval, sort and then merge intervals: O(nlogn) time
        # psuedo, then correct - O(n) solution
        # intervals is already sorted so I don't have to sort again
        start, end = newInterval # start and end that I am comparing current against
        merged = []
        i = 0
        for i,interval in enumerate(intervals):
            # insert everything non-overlapping before newInterval
            curr_start,curr_end = interval
            if curr_end < start:
                merged.append(interval)
            # new interval can be inserted here bc curr start > end: it will be between merged[-1] and curr
            elif curr_start > end:
                break
            # merge overlaps into each other and set that as newInterval to add
            elif start <= curr_end and curr_start <= end:
                newInterval = [min(curr_start,start),max(curr_end,end)]
                start,end = newInterval # set start/end as new interval to update comparison
        
        else: # if loop completed normally, move i to the next interval to include
            i = i + 1
        
        # insert new interval
        merged.append(newInterval)

        # insert everything non-overlapping after newInterval
        if i < len(intervals):
            merged.extend(intervals[i:])
        return merged

# [[1,3],[6,9]]
#         i
# [2,5]
# merged = [[1,5]]