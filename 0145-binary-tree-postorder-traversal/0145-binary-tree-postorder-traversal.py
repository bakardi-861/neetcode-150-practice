# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # I got the recursive solution, but I need to do it iteratively
        def helper(root, res):
            if root:
                helper(root.left, res)
                helper(root.right, res)
                res.append(root.val)
        
        res = []
        helper(root,res)
        return res