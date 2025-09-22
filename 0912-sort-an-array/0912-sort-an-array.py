class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #      l
        #        r
        # [1,2,5,9]
        #        p
        #      lt
        #        g 
        #        i

        def quicksort(l,r): # indices are inclusive
            if r-l+1 == 0 or r-l+1 == 1:
                return
            pivot = nums[random.randint(l,r)]
            lt, gt, i = l,r,l
            
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt],nums[i] = nums[i],nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt],nums[i] = nums[i],nums[gt]
                    gt -= 1
                else: # i == pivot
                    i += 1
            
            quicksort(l,lt-1)
            quicksort(gt+1,r)

        quicksort(0,len(nums)-1)
        return nums

    


        
