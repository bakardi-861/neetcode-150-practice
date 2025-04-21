# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # edge cases: multiple values .next are the node to remove (example 3), val to remove is not present (list traverses as normal), empty list (example 2)
        # need to do while curr.next.val = val

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next