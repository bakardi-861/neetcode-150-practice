class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quickselect O(n^2) in worse case, O(n) best, O(1) space
        # heap = O(nlogn), O(n) space

        # [3,2,1,5,6,4] -> [1,2,3,4,5,6]

        #heap
        # heap = nums
        # heapify(heap)

        # while len(heap) > k:
        #     heappop(heap)
        # return heap[0] if heap else -1

        # quickselect
        k = len(nums) - k
        l,r = 0,len(nums)-1
        while l <= r:
            lt,gt,i = l,r,l
            pivot = nums[random.randint(l,r)]

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt],nums[i] = nums[i],nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt],nums[i] = nums[i],nums[gt]
                    gt -= 1
                else:
                    i += 1
            
            if k < lt:
                r = lt - 1
            elif k > gt:
                l = gt + 1
            else:
                return nums[k]