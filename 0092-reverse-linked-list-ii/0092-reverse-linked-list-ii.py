# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(head,k):
            prev,curr = None,head
            while k:
                curr.next,prev,curr = prev,curr,curr.next
                k -= 1
            return (prev,curr)

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        for i in range(left-1):
            prev = prev.next

        start = prev.next
        curr = start
        k = right-left+1
        new_head, new_tail = reverse(curr,k)

        prev.next = new_head
        start.next =  new_tail

        return dummy.next
