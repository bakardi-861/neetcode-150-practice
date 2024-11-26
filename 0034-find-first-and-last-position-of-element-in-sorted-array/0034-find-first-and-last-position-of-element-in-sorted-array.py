class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)
        while l < r:
            m = (r+l)//2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        
        first = l
        if first == len(nums) or nums[first] != target:
            return [-1,-1]
        
        r = len(nums)-1
        while l < r:
            m = (l+r+1)//2
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        return [first, l]
