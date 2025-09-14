class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         # prefix sums?
        
        ans = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            ans[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in reversed(range(len(nums))):
            ans[i] *= suffix
            suffix *= nums[i]
        return ans