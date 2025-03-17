class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)*2
        ans = [0] * n

        for i in range(n//2):
            ans[i] = nums[i]
            ans[i+(n//2)] = nums[i]
        return ans