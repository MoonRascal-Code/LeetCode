class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = [] 
        def dfs(elements,start,end):
            if end == 0:
                result.append(elements[:])
                return 
            
            for i in range(start,n+1):
                elements.append(i)
                dfs(elements,i+1,end-1)
                elements.pop()
        
        dfs([],1,k)
        return result