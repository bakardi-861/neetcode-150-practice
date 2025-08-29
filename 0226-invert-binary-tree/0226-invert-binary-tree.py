# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # invert = swap children of each node
        # bfs, swap each child at each level? this swaps each subtree
        if not root: 
            return None

        q = deque([root])
        
        # [4,2,7,1,3,6,9]
        # q = []
        # res = [4,7,2,9,6,3,1]

        while q:
            for i in range(len(q)):
                node = q.popleft()

                node.left,node.right = node.right,node.left
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
