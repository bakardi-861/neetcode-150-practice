class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q,min_q = deque(),deque()
        l = 0
        longest = 0
        for r,num in enumerate(nums):
            #while to handle duplicates
            while max_q and num > max_q[-1]:
                max_q.pop()
            max_q.append(num)
            while min_q and num < min_q[-1]:
                min_q.pop()
            min_q.append(num)

            while max_q[0] - min_q[0] > limit:
                if nums[l] == min_q[0]:
                    min_q.popleft() 
                if nums[l] == max_q[0]:
                    max_q.popleft()
                l += 1
            longest = max(r-l+1,longest)
        return longest