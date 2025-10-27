class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # longest subarray = sliding window
        # limit = k
        # absolute diff = max abs diff
        # nums = [10,1,1,1,7,2], limit = 5
        #            l
        #                r
        # r = 5
        # window = {10:1} 
        # max_num = 7 # how would i do when shifting left?
        # min_num = 2
        # max_abs_diff = abs(7-2) = 5
        # limit = 5
        # longest = 4

        longest = 0
        l = 0 
        min_heap = []
        max_heap = []

        for r in range(len(nums)):
            heappush(min_heap,(nums[r],r)) # O(logn)
            heappush(max_heap,(-nums[r],r))

            # move l 
            while -max_heap[0][0] - min_heap[0][0] > limit:
                l = min(max_heap[0][1],min_heap[0][1]) + 1
                while max_heap[0][1] < l:
                    heappop(max_heap)
                while min_heap[0][1] < l:
                    heappop(min_heap)

            longest = max(longest, r-l+1)
        return longest