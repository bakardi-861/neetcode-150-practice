class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        result = []
        
        while i < n:
            new_start,new_end = newInterval
            curr_start,curr_end = intervals[i]
            if curr_end < new_start:
                result.append(intervals[i])
            elif curr_start > new_end:
                break
            else:
                #Overlap : merge them
                newInterval = min(new_start, curr_start),max(new_end, curr_end)
            i += 1
        
        result.append(newInterval)
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result