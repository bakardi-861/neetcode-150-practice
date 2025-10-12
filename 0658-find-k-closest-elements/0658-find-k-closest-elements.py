class Solution:
    def findClosestElements(self, nums, K, X):
        heap = []
        for num in nums:
            diff = abs(X - num)
            heappush(heap, (-diff, -num))  # store negated values for max-heap behavior
            if len(heap) > K:
                heappop(heap)
        
        return sorted([-num for _, num in heap])
