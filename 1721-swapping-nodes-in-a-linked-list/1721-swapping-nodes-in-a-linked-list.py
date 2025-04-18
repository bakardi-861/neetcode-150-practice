# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # kth from beginning = fast after moving it k places ahead
        # slow ends k places from the end
        # k = 1 2 3 4 5 
        #     [1,2,3,4,5]
        #              f
        #            s

        slow = fast = head
        k -= 1
        while k:
            k -= 1
            fast = fast.next
        
        start_k = fast
        sk = start_k.val

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        end_k = slow
        ek = end_k.val

        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        while curr:
            if curr == start_k:
                curr.val = ek
            elif curr == end_k:
                curr.val = sk
            curr = curr.next
        return dummy.next


        



