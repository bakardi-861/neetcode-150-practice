# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def dfs(root,path):
            nonlocal paths

            if not root:
                return
            
            path.append(root.val)

            if not root.left and not root.right:
                paths.append("->".join(map(str, path)))
                path.pop() #  pop root after finding answer
                return
            
            dfs(root.left,path)
            dfs(root.right,path)
            path.pop() # pop root after exploring subtrees
            return

        dfs(root,[])
        return paths