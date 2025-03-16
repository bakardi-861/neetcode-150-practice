class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap - store diff of target and current num. 
        # return True when we encounter that difference as a number in nums.
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[nums[i]] = i
        # return [-1,-1]