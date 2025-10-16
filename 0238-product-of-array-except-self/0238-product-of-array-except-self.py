class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
       
        left, right = 1, 1
        for i in range(len(nums)):
            ans[i] *= left
            ans[~i] *= right
            
            left *= nums[i]
            right *= nums[~i]
            
        return ans