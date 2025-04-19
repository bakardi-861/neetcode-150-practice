# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find the middle using slow/fast
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev, curr = None, slow.next
        slow.next = None  # Cut the list in half
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next,second.next = second,tmp1
            first, second = tmp1, tmp2
