class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lt,gt,i = 0,len(nums)-1,0
        
        while i <= gt:
            if nums[i] == 0:
                nums[lt],nums[i] = nums[i],nums[lt]
                lt += 1
                i += 1
            elif nums[i] == 2:
                nums[gt],nums[i] = nums[i],nums[gt]
                gt -= 1
            else:
                i += 1
        return nums