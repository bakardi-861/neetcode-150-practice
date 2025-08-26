class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #   0.1 2 3 4 5. 6
        # [-1,0,3,5,9,12]
        #  l      m      r
        
        l,r = 0,len(nums)
        while l < r:
            mid = (r+l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] >= target:
                r = mid
        return l if nums[l] == target else -1