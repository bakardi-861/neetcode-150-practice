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

        # array as a hashmap trick
        # if nums[i] < 0, i += 1
        # all negative numbers will end up going further right
        
        # if min exists, increment it.
        # in the 2nd loop if nums[i] is a negative number or nums[i] > min, then return min
        # check if duplicate, then swap with i-1 spot.
        #  0 1  2 3
        # [4,4,-1,1]
        # [1,-1,4,4]
        #     i
        #     j 

    
        n = len(nums)
        
        # Step 1: clean invalids
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n+1 # this puts all numbers out of bounds/negative numbers at the end
        
        # Step 2: place numbers in correct index
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: find missing
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
