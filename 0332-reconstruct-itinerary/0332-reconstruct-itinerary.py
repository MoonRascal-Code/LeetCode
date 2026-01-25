class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # graph 
        graph = collections.defaultdict(list)
        s_tickets = sorted(tickets,reverse=True)
        for start,end in s_tickets:
            graph[start].append(end)

        def dfs(s_name):
            while graph[s_name]:
                dfs(graph[s_name].pop())
            result.append(s_name)
        
        result = [] 
        dfs("JFK")
        return result[::-1] # 재귀이기 때문에 