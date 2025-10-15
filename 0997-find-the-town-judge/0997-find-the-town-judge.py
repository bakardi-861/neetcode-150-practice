class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # judge has no outgoing edges
        # n-1 incoming edges to the judge
            # return immediately
        
        indegree = [0] * (n+1)
        outdegree = [0] * (n+1)
        # graph = [[] for _ in range(n+1)]

        # [1]->[2]
     
        # # g = [[][2][]]
        # in = [0,0,1]
        # out = [0,1,0]

        for s,d in trust:
            # graph[s].append(d)
            indegree[d] += 1
            outdegree[s] += 1

        for i in range(len(indegree)):
            if indegree[i] == n-1 and outdegree[i] == 0:
                return i
        return -1

        

