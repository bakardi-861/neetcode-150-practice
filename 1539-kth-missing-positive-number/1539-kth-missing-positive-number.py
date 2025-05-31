class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # clarifying questions: 
            # is it the missing positive number in the consecutive sequence?
            # ex. 2 3 4 7 11 -> missing number is 5 because of 2 3 4 being a sequence and 7 not being a consecutive number
            # naive solution: iterate from 1 to arr[-1] + k and fill a list of all missing numbers and return the k-1th index when we find it. O(n^2) time and O(k) space.
            # less than O(n) time complexity: binary search O(logn) - works bc array is sorted
        # assumptions:
            # k can be any number from 1 to 1000
            # k will be a valid missing number

        # I just didn't read the problem. It's the kth missing positive number in the sequence, so we have to search over the range from the minimum positive number to the max positive number and find the kth missing one.
        # So how do I find which one is the kth missing one?
        # Do I binary search over the list of missing numbers to find the kth one? That would require an O(n) operation to create the list of missing nums though.

        # Once I determine if mid is a missing number, how do I know whether to move left or right??

        # O(n^2) solution
        # arr = [2,3,4,7,11], k = 5
        # min = 1
        # max = arr[-1] + k = 16

        # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
        #                 i - stop here since we found k

        # count = 5 res = 9
        # return res
        
        max_range = arr[-1] + k + 1
        count = 0
        res = -1
        for i in range(1,max_range):
            if i not in arr:
                count += 1
            if count == k:
                res = i
                return res

        # Got the naive solution in the first 5 or 6 minutes, but was struggling with the binary search solution for 16 minutes. Wrote the naive so that I would at least have that.
