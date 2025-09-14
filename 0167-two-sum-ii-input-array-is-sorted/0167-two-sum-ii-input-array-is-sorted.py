class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Output: array of both indices + 1
        # 2 pointers both ends
        # if sum < target, l + 1
        # if sum > target, r - 1
        # if pointers meet, no solution

        l,r = 0,len(nums)-1
        while l < r:
            sum = nums[l] + nums[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l+1,r+1]
        return [-1,-1] # no solution