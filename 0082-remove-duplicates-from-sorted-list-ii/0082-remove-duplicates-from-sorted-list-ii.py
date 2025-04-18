# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)
        dummy.next = head
        curr = head
        prev = dummy
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                duplicate_val = curr.val
                while curr and curr.val == duplicate_val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return dummy.next