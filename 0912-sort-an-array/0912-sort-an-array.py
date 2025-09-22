class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # learn merge sort
        # try heap sort
        # try counting/bucket sort
        # learn radix sort

        # heap sort
        heapify(nums)
        sorted_nums = [heappop(nums) for i in range(len(nums))]
        return sorted_nums