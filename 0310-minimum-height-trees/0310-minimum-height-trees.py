class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        graph = collections.defaultdict(list)

        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        leaves = [] 
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = [] 
            for i in leaves:
                neighbor = graph[i].pop()
                graph[neighbor].remove(i)
                
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves
        return leaves
