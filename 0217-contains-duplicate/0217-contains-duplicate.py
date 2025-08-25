class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n) time and space - set(nums) != len(nums)
        # O(nlogn) time, O(1) space - sort
        
        # [1,1,2,3]
        #     i
        
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                return True
            i += 1
        return False
