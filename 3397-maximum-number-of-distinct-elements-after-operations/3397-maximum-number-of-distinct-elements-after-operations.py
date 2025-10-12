class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        next_free = float('-inf')
        ans = 0

        for num in nums:
            low, high = num - k, num + k
            assign = max(next_free, low)
            if assign <= high:
                ans += 1
                next_free = assign + 1  # next number must be bigger to be distinct

        return ans
