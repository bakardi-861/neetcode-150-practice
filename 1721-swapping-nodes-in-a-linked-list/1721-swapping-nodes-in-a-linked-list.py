# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # naive: copy list, reverse, and get kth node from the end (4) and swap with kth node from beginning in original list (2).
        # fast/slow, move fast k steps ahead. move fast/slow one at a time until fast.next is null.

        dummy = ListNode(0)
        dummy.next = head

        start = end = head
        for _ in range(k-1):
            start = start.next
# only need to traverse the list once so start curr at start.next and when it reaches the end, "end" will be the kth from the end.
# this is because we moved start k steps ahead
        curr = start.next 
        while curr:
            end = end.next
            curr = curr.next
        
        start.val,end.val = end.val,start.val
        return dummy.next
