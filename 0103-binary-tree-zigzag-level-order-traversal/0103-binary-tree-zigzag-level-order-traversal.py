# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # for each odd level, append to result in reverse order
        if not root:
            return []
        
        q = deque([root])
        res = []
        level = 0

        while q:
            level_nodes = []
            for i in range(len(q)):
                curr = q.popleft()
                
                level_nodes.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if level % 2 == 1:
                level_nodes = level_nodes[::-1]
            res.append(level_nodes)
            level += 1
        return res