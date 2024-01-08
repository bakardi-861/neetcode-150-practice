class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range (len(nums)):
            comp = target - nums[i]
            if comp not in map:
                map[nums[i]] = i
            else:
                return [map[comp], i]