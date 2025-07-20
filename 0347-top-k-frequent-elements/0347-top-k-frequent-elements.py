class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = Counter(nums) #{1:3,2:2,3:1}
        heap = []
        heapq.heapify(heap)
        for num in hmap:
            heappush(heap,[hmap[num],num])
            if len(heap) > k:
                heappop(heap)
        res = []
        for n in heap:
            res.append(n[1])
        return res
