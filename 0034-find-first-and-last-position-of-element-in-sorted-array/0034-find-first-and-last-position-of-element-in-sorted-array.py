class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first():
            l,r = 0,len(nums)-1
            while l < r:
                mid = (r+l)//2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l if l < len(nums) and nums[l] == target else -1
        
        def find_last():
            l,r = 0,len(nums)-1
            while l < r:
                mid = (r+l+1)//2
                if nums[mid] <= target:
                    l = mid
                else:
                    r = mid-1
            return l if l < len(nums) and nums[l] == target else -1
        
        return [find_first(),find_last()]