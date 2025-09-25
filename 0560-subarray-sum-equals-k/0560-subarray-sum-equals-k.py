class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [0,1,2,3]
        
        total = 0
        prefix = [0] * (len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]

        seen = {0:1}
        for i in range(1,len(nums)+1): # k = 2
            diff = prefix[i] - k
            if diff in seen:
                total += seen[diff]
            seen[prefix[i]] = seen.get(prefix[i], 0) + 1 # either we've seen it already or it's the first time
        return total
