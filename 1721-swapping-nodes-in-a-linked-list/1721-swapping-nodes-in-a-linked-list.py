# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # naive: copy list, reverse, and get kth node from the end (4) and swap with kth node from beginning in original list (2).
        # fast/slow, move fast k steps ahead. move fast/slow one at a time until fast.next is null.
        # slow will be at kth from the end
        # when i == k, swap values, break and return??

        # [1,2,3,4,5]
        #    h
        #        s

        dummy = ListNode(0)
        dummy.next = head

        fast = slow = head
        for _ in range(k-1):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        for i in range(k):
            if i == k-1:
                head.val,slow.val = slow.val,head.val
            head = head.next
        return dummy.next
