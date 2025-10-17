# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # og left child becomes new root
        # og root becomes right child
        # og right child becomes left
        # everything is kind of shifted in a trinagle pattern
        # level by level - BFS
            # tree size is only 10, so could do backtracking?
        # every right node has a sibling (left node with same parent) and no children. 
            # og right children are always leaves

        if not root: return None
        curr = root
        prev,next,old_right = None,None,None
        while curr:
            next = curr.left
            curr.left = old_right
            old_right = curr.right
            curr.right = prev
            prev = curr
            curr = next
        return prev

