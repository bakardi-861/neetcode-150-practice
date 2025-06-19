# from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 2 ptrs in a sliding window kind of way because we want indices that are abs(i-j) <= k
        l = 0
        # win = defaultdict(int) # might not even need this part for this
        for r in range(1,len(nums)): #distinct indices
            # win[r] += 1

            # shrink window when abs value too big
            if abs(r-l) > k:
                # win[l] -= 1
                #if win[l] == 0: del win[l]
                l += 1
            # valid window found
            if l < r and nums[l] == nums[r]:
                return True
        return False
