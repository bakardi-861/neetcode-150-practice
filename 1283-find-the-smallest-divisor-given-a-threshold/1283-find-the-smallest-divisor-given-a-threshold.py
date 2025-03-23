class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def condition(d):
            total = 0
            for n in nums:
                total += ceil(n/d)
                if total > threshold:
                    return False
            return True

        l,r = 1,max(nums)
        while l < r:
            mid = (r+l) // 2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
        return l