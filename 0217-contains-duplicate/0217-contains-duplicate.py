class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sort and for loop - O(nlogn) time, O(1) space
        # set - O(n) time and space

        #sort
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                return True
        return False

        #set 
        # dupes = set()
        # for n in nums:
        #     if n in dupes:
        #         return True
        #     dupes.add(n)
        # return False