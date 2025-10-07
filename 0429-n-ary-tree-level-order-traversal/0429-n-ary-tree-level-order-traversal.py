"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        
        q = deque([root])
        res = []

        while q:
            level_list = []
            for _ in range(len(q)):
                node = q.popleft()
                level_list.append(node.val)
                q.extend(c for c in node.children if c)
            res.append(level_list)
        return res
                