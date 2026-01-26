class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 0. 그래프 
        graph = collections.defaultdict(list)
        for sta,arr,time in times:
            graph[sta].append((arr,time))
        
        # Q 변수, dist
        Q = [(0,k)] # (시간, 도착지)
        dist = collections.defaultdict(int) # 도착지, 시간 

        # 정렬 
        while Q:
            time, arr = heapq.heappop(Q)
            if arr not in dist:
                dist[arr] = time 
            
        # 추가
                for ar, tm in graph[arr]:
                    alt = tm + time 
                    heapq.heappush(Q,(alt,ar))

        # 추출 및 모든 노드 방문 확인 
        if len(dist) == n:
            return max(dist.values())
        return -1 



