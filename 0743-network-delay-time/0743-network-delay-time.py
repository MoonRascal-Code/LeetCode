class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. 모든 노드가 신호를 받는데 걸리는 시간 
        # 1-1 그래프화  { node : ( vertex, dist)}
        graph = collections.defaultdict(list)
        for s, v, d in times:
            graph[s].append((v,d))
        # 1-2 큐 변수 정의 및 거리 변수 정의 
        Q = [(0,k)] 
        # 거리, vertex -> 최소 heaq 모듈을 활용하여, 최소 경로를 구하기 위해 
        dist = collections.defaultdict(int)
        # 1-3 큐 순회 
        while Q: 
            time, vertex = heapq.heappop(Q)
            if vertex not in dist:
                dist[vertex] = time
                for v,d in graph[vertex]:
                    alt = time + d
                    heapq.heappush(Q,(alt,v))
            
        # 2. 모든 노드에 도달할 수 있는지 여부 
        if n == len(dist):
            return max(dist.values())
        
        return -1