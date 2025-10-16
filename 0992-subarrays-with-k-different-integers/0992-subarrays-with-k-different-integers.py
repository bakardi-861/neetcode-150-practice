from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # Helper: counts subarrays with at most K distinct integers
        def atMostK(nums, K):
            count = Counter()
            res = l = 0
            for r, num in enumerate(nums):
                count[num] += 1
                while len(count) > K:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1
                res += r - l + 1
            return res

        # Exactly K = atMostK(K) - atMostK(K-1)
        return atMostK(nums, k) - atMostK(nums, k-1)
