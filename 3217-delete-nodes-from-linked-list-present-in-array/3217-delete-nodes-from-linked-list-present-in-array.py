# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        #     set = {1}
        #     [1,2,1,2,1,2]
        #                 c
        # # create new node when c not in nums
        # ans = 0 - 2 - 2 - 2
        # O(n) time O(m) space

        dummy = ListNode(0)
        res = dummy
        curr = head
        nums = set(nums)
        while curr:
            if curr.val not in nums:
                res.next = ListNode(curr.val)
                res = res.next
            curr = curr.next
        return dummy.next