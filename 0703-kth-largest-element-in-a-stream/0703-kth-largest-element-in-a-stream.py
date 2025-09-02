# Heap
# quickselect

# [4,5,8,2] -> [4,5,8]
# k = 3

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # heapify nums
        self.heap = nums
        heapify(nums)

        # adjust heap to be of size k
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap,val)

        # adjust heap to be of size k
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)