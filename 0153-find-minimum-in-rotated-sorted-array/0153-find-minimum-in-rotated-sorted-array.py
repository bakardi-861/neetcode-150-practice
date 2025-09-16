class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l < r:
            mid = (r+l)//2 # mid will have left bias
            # partition check
            # left part
            if nums[mid] > nums[r]:
                l = mid + 1
            # right part
            else:
                r = mid
        return nums[l]