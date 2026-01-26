class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph 화 
        graph = collections.defaultdict(list)
        for s,e in prerequisites:
            graph[s].append(e)
        # 순환 구조 판별을 위한 set 
        traced = set() 
        visited = set() 

        def dfs(i):
            # 순환 구조면 False 
            if i in traced:
                return False 

            if i in visited:
                return True 
            
            traced.add(i) # 0 , 1 ,2 / 0, 2  
            for y in graph[i]:
                if not dfs(y):
                    return False 
            traced.remove(i)
            visited.add(i)
            return True 

        for x in list(graph):
            if not dfs(x):
                return False  

        return True 

