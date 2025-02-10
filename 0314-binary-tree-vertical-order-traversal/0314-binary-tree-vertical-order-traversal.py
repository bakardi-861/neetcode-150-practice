# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root,0)])
        d = defaultdict(list)
        c = 0
        minCol, maxCol = 0,0

        while q:
            for i in range(len(q)):
                curr,c = q.popleft()
                d[c].append(curr.val)

                minCol = min(minCol, c)
                maxCol = max(maxCol, c)

                if curr.left:
                    q.append((curr.left,c-1))
                    
                if curr.right:
                    q.append((curr.right,c+1))
        res = []
        for i in range(minCol,maxCol+1):
            res.append(d[i])
        return res
