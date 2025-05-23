# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeSort(arr, s, e,):
            # if 1 element remains, return left-most list
            if s == e:
                return lists[s]
            
            m = (s+e)//2
            left = mergeSort(arr, s, m)
            right = mergeSort(arr, m + 1, e)
            
            # Merge the two halves
            return merge2Lists(left, right)

        def merge2Lists(l1,l2):
            dummy = merged = ListNode(0, None)
            while l1 and l2:
                if l1.val <= l2.val:
                    merged.next = l1
                    l1 = l1.next
                else:
                    merged.next = l2
                    l2 = l2.next
                merged = merged.next

            if l1:
                merged.next = l1
            if l2:
                merged.next = l2
            return dummy.next

        # if lists is empty or there is only 1 empty list in lists
        if not lists or (len(lists) == 1 and not lists[0]):
            return None

        return mergeSort(lists, 0, len(lists)-1)


        
        


