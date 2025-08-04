# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        if not root:
            return 0

        q = deque([root])
        min_depth = float("inf")
        level = 1

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if not node.left and not node.right:
                    min_depth = min(min_depth,level)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return 0 if min_depth == float("inf") else min_depth
