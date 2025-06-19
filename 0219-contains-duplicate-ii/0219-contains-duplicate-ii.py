# from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # we want distinct indices that are abs(i-j) <= k
        l = 0
        win = defaultdict(int)
        second_index = -1
        for r in range(len(nums)): #distinct indices
            if nums[r] not in win:
                win[nums[r]] = r
            else:
                second_index = win[nums[r]]


            # shrink window when abs value too big
            if len(win) > k:
                if l == second_index:
                    second_index = -1
                del win[nums[l]]
                l += 1
            # valid window found
            if second_index != -1 and nums[second_index] == nums[r]:
                return True
        return False
