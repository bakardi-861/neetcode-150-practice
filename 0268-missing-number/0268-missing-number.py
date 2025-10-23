class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = nums[-1]
        for i in range(n+1):
            if nums[i] != i:
                return i
        return i+1