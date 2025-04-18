# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # create copy, reverse copy and return reversed_head == head
        # probably a 2 ptrs solution with fast/slow pointers
        def reverse(head):
            prev,curr = None, head
            while curr:
                curr.next,prev,curr = prev,curr,curr.next
            return prev

        dummy = ListNode(0)
        dummy.next = head
        
        slow = fast = dummy.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow = reverse(slow)

        first = head
        second = slow
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True