# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1,2,3,4,5] n = 2 (2-1) = 1
        #      n-1            # n = 4 (5-1)
        # 3 passes to reverse, n-1.next.next, then reverse again.
        # 2 passes to count nodes, n-1.next.next and return

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        for i in range(count-n):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next
        

