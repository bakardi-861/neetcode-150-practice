class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        mono_de = mono_in = True
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                mono_de = False
            if nums[i] < nums[i-1]:
                mono_in = False
        return mono_de or mono_in