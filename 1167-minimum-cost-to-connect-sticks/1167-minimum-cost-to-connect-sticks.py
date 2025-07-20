class Solution:
    def connectSticks(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        total = 0
        heapq.heapify(nums) # minheap
        while len(nums) >= 2:
            one,two = heapq.heappop(nums), heapq.heappop(nums)
            cur_sum = one + two
            total += cur_sum
            heapq.heappush(nums,cur_sum)
        return total