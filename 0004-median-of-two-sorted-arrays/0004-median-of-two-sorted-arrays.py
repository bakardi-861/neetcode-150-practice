class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge sort?? - Time: O(m+n), Space: O(m+n)
        # binary search?? how can i binary search 2 arrays? - O(log(min(m,n)))
        merged = []
        i,j = 0,0

        # merge 2 sorted lists
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # append remaining elements to merged
        # solution used a while loop but i wondered if this was easier
        if i < len(nums1):
            merged.extend(nums1[i::])
        if j < len(nums2):
            merged.extend(nums2[j::])
        
        # calculate median
        mid = len(merged) // 2
        if len(merged) % 2 == 0:
            return (merged[mid-1] + merged[mid]) / 2
        else:
            return merged[mid]



