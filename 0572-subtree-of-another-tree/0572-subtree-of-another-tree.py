# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # start when subroot == root
        # same tree from there, if same tree, then it is a subtree of another tree
        if not root:
            return False
        if not subRoot: # empty subtree is always a subtree
            return True

        def sameTree(root,sub):
            # both None
            if not root and not sub:
                return True
            # either None
            if not root or not sub:
                return False
            # diff value
            if root.val != sub.val:
                return False
            # return left and right
            return sameTree(root.left,sub.left) and sameTree(root.right,sub.right)
        
         # if trees match at this node OR somewhere in left/right subtree
        return (sameTree(root, subRoot) or 
                self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))