# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # go as deep left as we can, return when we hit null, pop back up
        # then return the root
        # then go as deep right as we can, return when null

        # see if there's a way to do this all in one function
        def inorder(root,res):
            if root:
                inorder(root.left, res)
                res.append(root.val)
                inorder(root.right, res)

        res = []
        inorder(root, res)
        return res
        