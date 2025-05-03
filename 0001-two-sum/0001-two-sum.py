class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # difference/complement trick
        hashmap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [i,hashmap[diff]]
            hashmap[n] = i