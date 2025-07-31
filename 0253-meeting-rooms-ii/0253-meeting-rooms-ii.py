class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # merge intervals? no, don't need to merge
        # intervals = [[0,30],[5,10],[15,20]]
        # rooms =.       1.     2.     2.  
        # if interval[i][0] is less than interval[i-1][1], add new room.
        # else, can use same room so don't increment
        # O(nlogn) time, O(1) space
        # times must be sorted first

        # intervals:[[4,9],[4,17],[9,10]]
        # code returns 3, but i don't need 3 rooms because [9,10] can go in the same room as [4,9]

        # need to use minheap
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])  # sort by start time
        heap = []

        for start, end in intervals:
            if heap and start >= heap[0]:
                heapq.heappop(heap)  # room becomes free
            heapq.heappush(heap, end)  # allocate current meeting

        return len(heap)  # max rooms used at once