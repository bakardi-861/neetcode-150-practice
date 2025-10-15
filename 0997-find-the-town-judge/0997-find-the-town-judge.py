class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        outdegree = [0] * n
        indegree = [0] * n

        # in = [0,1,1]
        # out = [1,1,0]

        for s,d in trust:
            indegree[d-1] += 1
            outdegree[s-1] += 1

        for i in range(len(indegree)):
            if indegree[i] == n-1 and outdegree[i] == 0:
                return i+1
        return -1