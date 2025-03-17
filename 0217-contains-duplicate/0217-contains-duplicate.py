class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set or sorting
        return len(nums) != len(set(nums))