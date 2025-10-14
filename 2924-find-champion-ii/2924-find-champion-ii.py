class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # n nodes: 0 - n-1
        # directed acyclical graph
        # directed edge: team at source node stronger than destination node team, d team weaker than s team
        # Team champion if no team stronger than it, return champion. if no unique champ, return -1.
        # count each teams wins, return highest win else -1.

        # build adj list from s to d
        graph = defaultdict(list)
        indegree = [0] * n
        for s,d in edges:
            graph[s].append(d)
            indegree[d] += 1

        def dfs(start):
            visit = set([start]) # start at node 0?
            stack = deque([start])
            while stack:
                node = stack.pop()
                if node not in visit:
                    visit.add(node)
                for nei in reversed(graph[node]):
                    if nei not in visit:
                        visit.add(nei)
                        stack.append(nei)
            return visit

        candidates = [i for i in range(n) if indegree[i] == 0]
        for c in candidates:
            visit = dfs(c)
            if len(visit) == n:
                return c
        return -1

        