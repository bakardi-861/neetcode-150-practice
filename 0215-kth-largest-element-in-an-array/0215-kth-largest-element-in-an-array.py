class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap is O(n) time, O(k) space
        # quickselect is O(n) time, O(1) space
        # I know I can't remember it all, but see how much I can get
        k = len(nums)-k # needs to do this because quickselect finds the kth smallest, so kth largest would be "n-k" smallest
                        # In Example 1: 2nd largest element is the 4th smallest.
        l,r = 0,len(nums)-1
        while l <= r: # needs to be <=
            pivot = nums[(random.randint(l,r))]
            lt,gt,i = l,r,l

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

            # comlpetely forgot this part
            if k < lt:
                r = lt - 1
            elif k > gt:
                l = gt + 1
            else:
                return nums[k]