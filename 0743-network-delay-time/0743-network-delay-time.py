class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. 모든 노드가 신호를 받는데 걸리는 시간 
        # 그래프화 
        graph = collections.defaultdict(list)
        for node, vertex, time in times:
            graph[node].append([vertex,time])

        # 큐 변수 
        Q = [(0,k)] # time, node 
        dist = collections.defaultdict(int) # 거리 저장 용 

        # 큐 순회 
        while Q:
            time, node =heapq.heappop(Q)
            if node not in dist: 
                # dist 에 항상 최소 값만 저장되게 하기 위해서, 
                dist[node] = time
                for v,t in graph[node]:
                    alt = time + t 
                    heapq.heappush(Q,(alt,v))
        

        if len(dist.keys()) == n:
            return max(dist.values())

        return -1 

        # 2. 모든 노드에 도달할 수 있는지 여부 
