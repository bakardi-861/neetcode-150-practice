# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # keep track of path and node? [node, path_length]
        
        diameter = 0
        def dfs(root):
            nonlocal diameter
            if not root:
                return 0 # -1

            left_height = dfs(root.left)
            right_height = dfs(root.right) 

            diameter = max(diameter, left_height + right_height) # + 2
            return 1 + max(left_height,right_height)
        
        dfs(root)
        return diameter

        