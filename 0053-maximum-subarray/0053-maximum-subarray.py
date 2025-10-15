class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # naive: calculate the sum of every subarray and return the max
        # greedy: if we want the max, we want the largest numbers in the array in the subarray
        # if sum < max_so_far, move l
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum