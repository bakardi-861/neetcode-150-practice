class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        l,r = 0,0
        win = set()
        while r < len(nums):
            if nums[r] in win:
                return True

            win.add(nums[r])
            r += 1
            if abs(r-l) > k:
                win.discard(nums[l])
                l += 1
        return False