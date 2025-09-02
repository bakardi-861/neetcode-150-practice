# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p = [1,2,3]
        #      p
        # q = [1,2,3]
        #      q
        def dfs(p, q):
            # both are None → same
            if not p and not q:
                return True
            # only one is None → different
            if not p or not q:
                return False
            # values differ → different
            if p.val != q.val:
                return False
            # must check both subtrees
            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)


        