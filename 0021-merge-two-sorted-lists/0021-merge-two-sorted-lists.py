# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node
        dummy = ListNode(-1)
        # merged list = dummy
        merged = dummy

        # while l1 and l2 are not null
        while l1 and l2:
            # if l1.val is less than l2.val:
            if l1.val < l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            merged = merged.next

        # check if either list still has values and stitch them to the end of merged
        if l1:
            merged.next = l1
        if l2:
            merged.next = l2
        return dummy.next