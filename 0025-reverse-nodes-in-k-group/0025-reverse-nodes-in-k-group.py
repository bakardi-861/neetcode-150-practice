# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head,k):
            prev,curr = None, head
            while k:
                curr.next,prev,curr = prev,curr,curr.next
                k -= 1
            return (prev,start,curr)
            
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next
        
        while n >= k:
            start = group_prev.next
            nodes = reverse(start,k)
            new_head,new_tail,next_group_start = nodes[0],nodes[1],nodes[2]

            group_prev.next = new_head
            new_tail.next = next_group_start
            group_prev = new_tail
            
            n -= k
        return dummy.next
            
        
