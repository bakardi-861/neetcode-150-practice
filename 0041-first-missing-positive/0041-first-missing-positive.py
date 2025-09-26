class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # clarifying question: are we guaranteed to have all unique nums or are duplicates allowed?
        # skip nums < 0 since we have to check if 1 is missing if we have 0 and 2. ex. [0,2]
        # the missing number doesn't have to be consecutive with the rest, we just want the smallest positive number.
        # By default, the min is always 1 if we didn't find it in the array.
        # If 1 exists, increment the min until we find 2, and so on and so on.
        
        # BRUTE FORCE
        # sort: O(nlogn) time, q = O(n) space
        # sort num, store all positives in q
        # loop through q, popleft if min == q[0]. increment min. else return min.
        # q = [] 
        # min = 3
        # return min

        # no sorting and no q, topic says hash table but that's O(n) in the worst case?
        # naive is exponential time bc we'd have to check every num in the array to check for every possible min
        # skip negative nums
        # {3:1,4:1}
        #  i
        # min = 2

        pos_map = Counter()
        for n in nums:
            if n > 0:
                pos_map[n] += 1

        min = 1
        for key in pos_map:
            if min in pos_map and pos_map[min] > 0:
                pos_map[min] -= 1
                min += 1
            else:
                return min
        return min