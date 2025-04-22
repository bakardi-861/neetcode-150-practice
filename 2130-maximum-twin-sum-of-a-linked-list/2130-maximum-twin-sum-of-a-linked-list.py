# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # fast/slow, reverse second half and then get sum by adding alternating values
        # this works bc n is always even
        
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

        second = reverse(slow)
        first = head
        max_sum = 0
        first_sum = 0
        second_sum = 0

        # head = [5,4,2,1]
        # first = [4]
        # second = [2]
        # sum = 6

        
        while first and second: 
            sum = first.val + second.val
            max_sum = max(max_sum, sum)
            first = first.next
            second = second.next
        return max_sum