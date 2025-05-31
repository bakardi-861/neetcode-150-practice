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
        
        # max_range = arr[-1] + k + 1
        # count = 0
        # res = -1
        # for i in range(1,max_range):
        #     if i not in arr:
        #         count += 1
        #     if count == k:
        #         res = i
        #         return res

        # Got the naive solution in the first 5 or 6 minutes, but was struggling with the binary search solution for 16 minutes. Wrote the naive so that I would at least have that.
        # Wasted time on another solution that didn't work where I iterate through the range and the arr simultaneously, but ran into index out of bounds errors when the kth missing number is beyond the range of the arr.

        # I gave up after 22 minutes and watching the Cracking FAANG video
        # He gave the intuition that there are 3 cases:
        # 1. everything to the left of the first num in arr is missing -> return arr[0] - k
        # 2. everything to the right of the last num in arr in missing -> return arr[-1] + k
        # 3. mix of the two
        # basically if our first element is 4 for example, and k = 7, we know that 1,2, and 3 are missing already, so when we iterate through the arr, k = 4.
        # Compare nums[i] and nums[i+1]. If the difference between them is 1, then they aren't missing bc arr is sorted. Else, there is a missing number, so we do k -= difference.
        # If k == 0, return that num


        if arr[0] != 1:
            if arr[0] - 1 >= k:
                return k
            else:
                k -= arr[0] - 1
        i = 0
        while i < len(arr)-1:
            diff = arr[i+1] - arr[i]
            if diff != 1:
                for num in range(arr[i]+1,arr[i+1]):
                    k -= 1

                    if not k:
                        return num
            i += 1

        if k:
            return arr[-1] + k