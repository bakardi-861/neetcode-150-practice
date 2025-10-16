class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        # binary search to find x index
        # from x index, expand 2 ptrs outward
        l = bisect_left(nums,x) #??
        r = l
        while r - l < k:
            if l == 0:
                r += 1
            elif r == len(nums):
                l -= 1
            else: # check next l
                if abs(nums[l-1] - x) <= abs(nums[r]-x): 
                    l -= 1
                else:
                    r += 1
        return nums[l:r]