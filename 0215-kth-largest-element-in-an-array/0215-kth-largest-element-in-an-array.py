class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        l,r = 0,len(nums)-1
        while l <= r:
            pivot = nums[random.randint(l,r)]
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
            
            if k < lt:
                r = lt - 1
            elif k > gt:
                l = gt + 1
            else:
                return nums[k]
        return -1