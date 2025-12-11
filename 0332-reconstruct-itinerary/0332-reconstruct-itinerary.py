class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for a,b in sorted(tickets):
            graph[a].append(b)

        print("graph",graph)

        route,stack = [],["JFK"]

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
                print(stack)
            route.append(stack.pop())

        return route[::-1]