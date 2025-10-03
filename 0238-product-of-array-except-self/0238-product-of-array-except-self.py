class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n  # prefix[i] will hold product of elements to the left of i

        # Step 1: build prefix array without a separate run variable
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        # Step 2: multiply in suffix products using a running variable
        suffix = 1
        for i in reversed(range(n)):
            prefix[i] *= suffix
            suffix *= nums[i]

        return prefix