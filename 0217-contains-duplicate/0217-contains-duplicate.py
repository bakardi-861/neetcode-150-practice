class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sort and 2 pointers - O(nlogn) time, O(1) space
        # set - O(n) time and space

        #set 
        dupes = set()
        for n in nums:
            if n in dupes:
                return True
            dupes.add(n)
        return False