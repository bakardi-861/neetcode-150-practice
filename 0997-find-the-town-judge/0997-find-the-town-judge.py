class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1

        indegree = [0] * n
        outdegree = [0] * n

        for s, d in trust:
            outdegree[s - 1] += 1
            indegree[d - 1] += 1

        for i, indeg in enumerate(indegree):
            if indeg == n - 1 and outdegree[i] == 0:
                return i + 1

        return -1