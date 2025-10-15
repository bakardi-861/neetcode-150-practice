class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # judge has no outgoing edges
        # n-1 incoming edges to the judge
            # return immediately
        
        graph = [0 for _ in range(n+1)]

        # [1]->[2]

        # indegree - outdegree
        # n-1 - 0
     
        for s,d in trust:
            # graph[s].append(d)
            graph[s] -= 1
            graph[d] += 1

        for i in range(1,len(graph)):
            if graph[i] == n-1:
                return i
        return -1

        

