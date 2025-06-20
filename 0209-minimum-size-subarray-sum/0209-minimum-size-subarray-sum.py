class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # smallest subarray with sum >= target, else 0
        smallest = float("inf")
        l = 0
        win_sum = 0
        for r in range(len(nums)):
            win_sum += nums[r]
            # while we can potentially find a smaller subarray
            while win_sum >= target:
                smallest = min(smallest, r-l+1)
                win_sum -= nums[l]
                l += 1
        return 0 if smallest == float("inf") else smallest
