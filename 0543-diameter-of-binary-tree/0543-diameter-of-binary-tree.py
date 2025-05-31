# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter: length of the longest path between any two nodes, may/may not pass through root
        # length: number of edges between 2 nodes
        # DFS and keep track of current path and longest path, return the longest path

        # I keep getting 1 less than the correct answer for the 1 example because it's only counting [1,2,4] or [1,2,5] as a path and not [1,2,4,5] as a path for example.
        # When I pop back up and go down the right subtree, it doesn't add to the current path. It just removes the last left subtree root from the path.
        # Looked at CF video after 17 minutes

        # DFS to the leaves and build solution as we go up
        # need to be greedy

        self.diameter = 0
        self.dfs(root)
        return self.diameter

    def dfs(self,root):
        if not root:
            return 0
        
        # if root is a leaf, so add 1 to the path length
        if not root.left and not root.right:
            return 1
        
        l_length = self.dfs(root.left)
        r_length = self.dfs(root.right)

        # check if joining the left and right subtree lengths gives us a better max diameter
        self.diameter = max(self.diameter, l_length + r_length)

        # going up one level in the tree 
        return 1 + max(l_length,r_length)

        # T: O(n) - n is the num of nodes in the tree
        # S: O(n) - where n is the height of the tree/recursion stack