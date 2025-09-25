class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # subarry length (i-j+1) >= 2
        # subarray sum is a multiple of k (sum % k == 0)
        # if both cases are true, return True. Else False.

        n = len(nums)
        freq = {0:-1}
        prefix_sum = 0
        for i in range(n):
            prefix_sum += nums[i]
            res = prefix_sum % k

            if res in freq:
                if i - freq[res] >= 2:
                    return True
            else:
                freq[res] = i
        return False