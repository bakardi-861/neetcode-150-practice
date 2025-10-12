class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        index = bisect.bisect_left(nums, x)
        l, r = index - 1, index  # l points left, r points right

        while r - l - 1 < k:  # window size = r - l - 1
            if l < 0:
                r += 1
            elif r >= len(nums):
                l -= 1
            elif x - nums[l] <= nums[r] - x:
                l -= 1
            else:
                r += 1

        return nums[l+1:r]
