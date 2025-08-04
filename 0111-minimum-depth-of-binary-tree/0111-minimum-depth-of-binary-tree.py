# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        min_depth = float(inf)

        def dfs(root, depth):
            nonlocal min_depth
            if not root:
                return

            if not root.left and not root.right:
                min_depth = min(min_depth,depth)
                return

            dfs(root.left, depth+1)
            dfs(root.right, depth+1)

        dfs(root,1)
        return 0 if min_depth == float("inf") else min_depth

