class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # if current step sum == abs(nums[i]), end iteration and increment start value
        # this can get tedious if we have to increment many times
        # prefix sums to calculate sum so far?
        # nums = [-3,2,-3,4,2]
       # prefix = [0,-3,-1,-4,0,2]
       # 1 - min prefix sum = startvalue
    #    startValue + min_prefix_sum ≥ 1
    #     ⇒ startValue ≥ 1 - min_prefix_sum
    #     ⇒ startValue ≥ 1 - (-4) = 5

        total = 0
        min_sum = 0
        for num in nums:
            total += num
            min_sum = min(min_sum, total)
        return 1 - min_sum


