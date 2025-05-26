# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        # keep track of row and column of each node
        # root is (0,0) (row,col)
        # left subtree is row +1, col -1
        # right subtree is row +1, col +1
        # group nodes in the column in insertion order
        # in ex. 1, [3,15] is the group bc 3 is processed before 15.

        # bfs = O(n) - n number of nodes
        # space: O(n) storing n nodes
        # q = [] # (val,r,c)
        # val = 7
        # r = 2 # might not need
        # c = 2
        # col_order = {0:[3,0,1],-1:[9],1:[8],-2:[4],2:[7]}

        # need to always write this edge case
        if not root:
            return []

        q = deque([(root,0,0)])
        col_order = defaultdict(list)

        while q:
            for i in range(len(q)):
                node,r,c = q.popleft()
                col_order[c].append(node.val)

                if node.left:
                    q.append((node.left,r+1,c-1))
                if node.right:
                    q.append((node.right,r+1,c+1))

        col_order = sorted(col_order.items()) #O(nlogn)

        res = []
        for val in col_order: # append each list to res
            res.append(val[1])
        return res
        
