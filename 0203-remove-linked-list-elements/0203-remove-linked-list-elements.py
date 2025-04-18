# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # head = [1,2,6,3,4,5,6], val = 6
        #         c n
        # Output: [1,2,3,4,5]
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr:
            if curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return dummy.next