# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def findMin(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr

        if not root:
            return None
    
        if val < root.val:
            root.left = self.deleteNode(root.left, val)
        elif val > root.val:
            root.right = self.deleteNode(root.right, val)
        else:
            # check if it has at least 1 child
            # if 0 children, it will just return None for root.right
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else: # 2 children
                minNode = findMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root