# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # in one pass we can use a stack to store each node and we see its twin, calculate the sum. 
        # pop node from stack.
        # if it's the max so far, update the max.

        dummy = ListNode(0)
        dummy.next = head

        # get n (size of list)
        n = 0
        c = head
        while c:
            n += 1
            c = c.next


        stack = []
        max_sum = 0
        i = 0
        curr = head
        
        while curr and i < n:
            if stack and stack[-1][1] == n-1-i:
                sum = stack[-1][0] + curr.val
                max_sum = max(sum,max_sum)
                stack.pop()
            else:
                stack.append([curr.val,i])
           
            i += 1
            curr = curr.next
        
        return max_sum
