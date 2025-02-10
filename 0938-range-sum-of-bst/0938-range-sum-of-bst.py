# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return None
        
        q = deque([root])
        range_sum = 0

        while q:
            for i in range(len(q)):
                curr = q.popleft()

                if low <= curr.val <= high:
                    range_sum += curr.val
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return range_sum