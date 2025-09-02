class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # get the 2 heaviest stones with a maxheap
        # if x == y, pop both
        # if x != y, pop both, append (y-x) to heap
        # return the last stone left if heap is not empty, else 0.
        
        # [2,7,4,1,8,1] -> [-8,-7,-4,-2,-1,-1]
        
        heap = [-n for n in stones]
        heapify(heap)

        while len(heap) > 1:
            x,y = -heappop(heap),-heappop(heap)

            if x != y:
                heappush(heap,-abs(y-x))
        return -heap[0] if heap else 0

