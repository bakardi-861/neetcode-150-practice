class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # naive way to do this is to insert new interval, sort and then merge intervals: O(nlogn) time
        # psuedo, then correct - O(n) solution
        # intervals is already sorted so I don't have to sort again
        start, end = newInterval # split newInterval into start and end times
        merged = []
        # flag = False
        i = 0
        while i < len(intervals):
            # check if new interval can be inserted at current spot
            # insert everything before newInterval
            curr_start,curr_end = intervals[i]
            if curr_end < start:
                merged.append([curr_start,curr_end])
                # i += 1
            # new interval already merged/can be inserted here bc curr start > end
            elif curr_start > end: 
                break
            elif curr_start <= start <= curr_end or curr_start <= end <= curr_end:
                newInterval = [min(curr_start,start),max(curr_end,end)]
                start,end = newInterval
            i += 1
                # can't break here because we could still be able to merge the rest of the array

        # insert new interval
        merged.append(newInterval)

        # insert everything after newInterval at i
        if i < len(intervals):
            merged.extend(intervals[i:])
        return merged

# [[1,3],[6,9]]
#         i
# [2,5]
# merged = [[1,5]]