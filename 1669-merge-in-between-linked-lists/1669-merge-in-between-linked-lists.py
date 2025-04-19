# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
                        # a-1   b+1
                # ans = [...13,[list2],5]
        dummy = ListNode(0)
        dummy.next = list1

        prev = None
        curr = list1
        after = None

        for i in range(b+1):
            if i == a-1:
                prev = curr
            elif i == b:
                after = curr.next
            curr = curr.next
        
        prev.next = list2

        tail = list2
        while tail.next:
            tail = tail.next
        tail.next = after
        return dummy.next

