class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quickselect O(n^2) in worse case, O(n) best, O(1) space
        # heap = O(nlogn), O(n) space

        # [3,2,1,5,6,4] -> [1,2,3,4,5,6]

        #heap
        heap = nums
        heapify(heap)

        while len(heap) > k:
            heappop(heap)
        return heap[0] if heap else -1