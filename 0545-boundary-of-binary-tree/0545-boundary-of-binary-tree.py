class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        l, r, p = root.left, root.right, root
        if root.left or root.right: 
            res.append(root.val)
        # left boundary - since we append to list in order, we can just add left boundary answers directly to the result in order
        while l and (l.left or l.right): 
            res.append(l.val)
            if l.left:
                l = l.left
            else:
                l = l.right
        
        # leaves - get leaves by putting all nodes from tree in a q
        q = deque([p])
        while q:
            node = q.popleft()
            if node and not node.left and not node.right:
                res.append(node.val)
            # we add the children this way because we want the right child to get processed first
            # this is so leaves are in order
            if node.right:q.appendleft(node.right)
            if node.left:q.appendleft(node.left) 
        
        # right boundary
        rb = []
        while r and (r.left or r.right):
            rb.append(r.val)
            if r.right:
                r = r.right
            else:
                r = r.left
        res.extend(rb[::-1]) # this just adds right boundary to solution in reverse order
        return res