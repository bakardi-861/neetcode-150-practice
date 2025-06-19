class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # nums = [1,2,4], k = 0
        #         l
        #             r 
        # win = {1:0,2:0,4:3}
        # max_f = 3

        nums.sort()
        win = 0
        l = 0
        max_f = 0
        for r in range(len(nums)):
            win += nums[r]
            cost = (r-l+1) * nums[r] - win
            if cost > k:
                win -= nums[l]
                l += 1
            max_f = max(max_f,r-l+1) # since they will all be the same here
        return max_f

