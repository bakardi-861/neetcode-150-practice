# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # <-1 2->3->4->5
        #   c
        #     n
        #   p

        # curr = 1
        # next = null
        # prev = null
        
        curr,next,prev = head, None, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev