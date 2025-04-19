# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        def reverse(head):
            prev, curr = None, head
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

        first_half = head
        merged = dummy
        flag = True

        while first_half and second_half:
            if flag:
                merged.next = first_half
                first_half = first_half.next
                flag = False
            else:
                merged.next = second_half
                second_half = second_half.next
                flag = True
            merged = merged.next

        if first_half:
            merged.next = first_half
        elif second_half:
            merged.next = second_half
        return dummy.next