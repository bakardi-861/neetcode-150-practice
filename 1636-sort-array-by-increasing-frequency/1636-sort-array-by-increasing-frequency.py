class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # counting sort - constraint is 1-100.
        # sort in decreasing order when freqs are the same (need to keep track of previous frequency?)
        # sort in increasing order OF FREQUENCY

        # nums = [2,3,1,3,2]
        # counts = {1:1,2:2,3:2} # num:frequency
        # res = [1,3,3,2,2] # append num freq times
        # how do i switch and sort from decreasing wnen frequencies are the same?

        # None of this!
        # nums = [-1,1,-6,4,5,-6,1,4,1]
        # counts = {-1:1,1:3,-6:2,4:2,5:1}
        # # group numbers by frequency
        # min = 1, max = 3
        # freqs = {1:[-1],3:[1],2:[4,-6]} # heapify the lists?
        # for i in range(min,max+1):
            # for j in freqs[i]
        # append freqs[i][j] to res i times
        # res = [-1,4,4,-6,-6,1,1,1]
        # time: O(n + counts + freqs*k) where n = size of nums and k = length of longest freq list
        # space: O(n + freqs*k)

        # looked at hints after 16:43: Use a custom comparator to compare values by their frequency. If two values have the same frequency, compare their values.
        # nums = [-1,1,-6,4,5,-6,1,4,1]
        # counts = {-1:1,1:3,-6:2,4:2,5:1}
        counts = Counter(nums)
        nums.sort(key=lambda x: (counts[x], -x))
        return nums

            

