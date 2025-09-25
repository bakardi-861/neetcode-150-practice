class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # subarry length (i-j+1) >= 2
        # subarray sum is a multiple of k (sum % k == 0)
        # if both cases are true, return True. Else False.

        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        mod_map = {0:0}
        for j in range(1,n+1):
            curr_mod = prefix[j] # sum so far

            # check if sum is a multiple of k
            if k != 0:
                curr_mod %= k

            # if we have seen this sum that is a mult of k or sum=0 (since 0 is in the map by default), check the length of the current subarray
            if curr_mod in mod_map:
                if j - mod_map[curr_mod] >= 2:
                    return True
            else: # if we haven't seen this mult. of k, store the starting index
                mod_map[curr_mod] = j
        return False
