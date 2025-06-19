class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sliding = set()

        # if k = 0, then False because there can be no answer
        if k == 0:
            return False

        # add numbers to set up to k
        for c in nums[:k]:
            if c in sliding: # if we found a duplicate, then True
                return True
            sliding.add(c)

        # 
        for i in range(k, len(nums)):
            if nums[i] in sliding:
                return True
            # remove first item (l) from set if window too big
            sliding.discard(nums[i-k]) # does not raise an error if num not in set like .remove() does
            sliding.add(nums[i]) # add current to sliding window

        return False