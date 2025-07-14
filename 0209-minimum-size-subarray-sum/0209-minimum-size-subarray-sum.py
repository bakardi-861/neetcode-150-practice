class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # nums = [2,3,1,2,4,3]
        #                   r
        #                 l
        # target = 7
        # curr_sum = 7
        # min_len = inf, 4, 3, 2

        min_len = float(inf)
        l = 0
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                min_len = min(min_len,r-l+1)
                curr_sum -= nums[l]
                l += 1
        return min_len if min_len != float(inf) else 0