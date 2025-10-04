class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize slow and fast pointers
        slow, fast = head,head

        # Move slow one step and fast two steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Check if the fast meets the slow
            if slow == fast:
                break

        # Check if there is no cycle
        if not fast or not fast.next:
            return None

        # Reset either slow or fast pointer to the head
        fast = head

        # Move both pointers one step until they meet again
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Return the node where the cycle begins
        return slow