# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            prev,curr = None,head
            while curr:
                curr.next,prev,curr = prev,curr,curr.next
            return prev
        
        dummy = ListNode(0)
        dummy.next = head

        fast = slow = head
        prev = dummy
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        slow = reverse(slow)
        prev.next = None
        
        while head and slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True