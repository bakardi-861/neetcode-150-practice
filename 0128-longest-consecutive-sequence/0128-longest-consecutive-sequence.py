class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hash table: track sequence starts, if num-1 not in set
        # union find: connected component = consecutive sequence (num + 0 or num + 1 or num - 1)
        parent = {}
        size = {}

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY: return
            if size[rootX] < size[rootY]:
                rootX, rootY = rootY, rootX
            parent[rootY] = rootX
            size[rootX] += size[rootY]

        # initialize nodes
        for num in nums:
            parent[num] = num
            size[num] = 1

        # union consecutive neighbors
        for num in nums:
            if num - 1 in parent:
                union(num, num - 1)
            if num + 1 in parent:
                union(num, num + 1)

        return max(size.values(), default=0)
