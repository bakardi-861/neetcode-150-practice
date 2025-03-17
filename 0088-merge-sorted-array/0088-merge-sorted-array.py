class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # merge 2 sorted lists approach
        i,j,k = 0,0,0
        nums1_copy = nums1[::]
        while i < m and j < n:
            if nums1_copy[i] <= nums2[j]:
                nums1[k] = nums1_copy[i]
                i += 1
            elif nums2[j] <= nums1_copy[i]:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        
        if i < m:
            nums1[k:] = nums1_copy[i:]        
        if j < n:
            nums1[k:] = nums2[j:]