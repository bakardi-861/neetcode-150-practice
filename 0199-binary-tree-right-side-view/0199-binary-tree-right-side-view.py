# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root]) if root else None
        ans = []

        while q:
            levelSize = len(q)
            for i in range(len(q)):
                last = i == levelSize - 1
                curr = q.popleft()

                if last:
                    ans.append(curr.val)
                    
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return ans
