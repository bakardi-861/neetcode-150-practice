class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        copy_dict = {}
        st = [node]
        
        while st:
            n = st.pop()
            if n not in copy_dict:
                copy_dict[n] = Node(n.val, [])
            
            for nei in n.neighbors:
                if nei not in copy_dict:
                    copy_dict[nei] = Node(nei.val, [])
                    st.append(nei)
                copy_dict[n].neighbors.append(copy_dict[nei])
        
        return copy_dict[node]
