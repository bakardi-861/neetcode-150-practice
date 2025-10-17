# KEY: right child has no child! focus on left
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root, new_left, new_right):
            if root is None:
                return None

            # backup copies
            orig_left = root.left
            orig_right = root.right

            # update root's children
            root.left = new_left
            root.right = new_right

            # leaf is the new root
            if orig_left is None:
                return root

            # update left child recursively
            return dfs(
                root = orig_left, 
                new_left = orig_right, 
                new_right = root
            )            
        
        return dfs(root, None, None)        