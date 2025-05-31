class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # iterate with k = 0 and i = 0 to start
        # if nums[i] = 0, skip i ahead. if nums[i] != 0, swap nums[k] with nums[i].
        # by the time i reaches the end, all 0s will be at the end of the array
        # nums = [1,3,12,0,0]
        #             k
        #                 i

        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k],nums[i] = nums[i],nums[k]
                k += 1
        
