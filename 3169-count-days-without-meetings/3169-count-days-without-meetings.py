class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # days start from 1 and end at days ex. days = 10 is 1-10
        # meetings intervals represent start and end days of meetings (INCLUSIVE)
        # return how many days the employee is available for work and NOT in meetings.
        # Meetings may overlap!
        # Merge Intervals pattern

        # sort meetings by start/end date.
        # find lowest start date first
        # if current start is < prev end, swap the two.
        # if they curr start == prev end, merge them into a new interval: [prev start,curr end]
        # how do i delete the old intervals?
        # increment prev annd curr by 1

        # meetings = [[1,3],[5,7],[9,10]]
                                   #c
                              #p
        # now we have to iterate the sorted range of days to see which days do not appear
        # first interval end is 3, 2nd interval start is 5, meaning there is no 4.
        # 2nd interval end is 7, 3rd internal end is 9 meaning there is no 8.
        # Return 2
        # days = 10
        # O(n) time, O(1) space?

        # meetings = [[1,7],[9,10]] days = 12
        #                           c
        #                    p

        # meetings = [[1,6]] days = 6
        #                    c
        #               p 

        # 15:31 - psuedocode

        # fixes: -sort meetings by start time
            #    - use a merged array to store the result intervals

        meetings.sort()

        # meetings = [[1,3],[5,7],[9,10]]
        merged = []

        for m in meetings:
            # if meeting not merged or last end time in merged < current start
            if not merged or merged[-1][1] < m[0]:
                merged.append(m)
            else:
                # merge the two by updating the last end time in merged to be the larger of the two
                merged[-1][1] = max(merged[-1][1],m[1])

        # old code
        # prev, curr = meetings[0],None
        # for i in range(1, len(meetings)):
        #     curr = meetings[i]
        #     if curr[0] < prev[1]:
        #         meetings[i], meetings[i-1] = meetings[i-1],meetings[i]
        #     elif curr[0] == prev[1]:
        #         new_interval = [prev[0],curr[1]]
        #         # delete the old curr and prev intervals
        #         meetings[i] = new_interval
        
        res = 0

        if merged[0][0] > 1:
            res += merged[0][0] - 1

        for i in range(1,len(merged)):
            curr_start = merged[i][0]
            prev_end = merged[i-1][1]
            days_between = curr_start - prev_end
            if days_between > 1:
                res += days_between-1
        
        # add remaining days after last meeting
        res += (days - merged[-1][1])
        return res