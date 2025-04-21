# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # split in half, reverse 2nd half and return if first_half = second_half
        # this way we don't have to copy the entire list and reverse it
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
        
        prev.next = None
        second_half = reverse(slow)

        while head and second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        return True
