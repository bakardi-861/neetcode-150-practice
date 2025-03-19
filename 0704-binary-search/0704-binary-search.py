class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return first and last instance of target
        l,r = 0,len(nums)-1
        while l < r:
            mid = (r+l+1)//2 # need + 1 when finding last occurence to have a right bias

            if nums[mid] <= target: # target is larger than mid, or == mid
                l = mid
            else: # target is smaller than mid, shrink space
               r = mid - 1
        return l if nums[l] == target else -1
        #   0 1 2 3 4 5 
        # [-1,0,3,5,9,12].  target = 9
        #           m
        #           l
        #                 r