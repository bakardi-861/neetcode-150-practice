# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101, None) # dummy node
        merged = dummy
        while l1 and l2:
            if l1.val < l2.val:
                temp = l1.next
                merged.next = l1
                l1 = temp
            elif l2.val <= l1.val:
                temp = l2.next
                merged.next = l2
                l2 = temp
            merged = merged.next

        if l1:
            merged.next = l1
        if l2:
            merged.next = l2
        return dummy.next