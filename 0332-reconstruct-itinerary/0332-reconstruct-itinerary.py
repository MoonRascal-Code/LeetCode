class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. 사전 순이기 때문에, sorted(reverse)
        # 2. 그래프 생성 (dict)
        # 3. 오일러 법칙 
        res = [] 
        # 1,2 
        graph = collections.defaultdict(list)
        for start,end in sorted(tickets,reverse=True):
            graph[start].append(end)

        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            res.append(start)
        
        dfs("JFK")
        return res[::-1]
        

        
        