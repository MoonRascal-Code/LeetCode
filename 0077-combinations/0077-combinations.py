class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(elements,num,length):
            if length == 0:
                result.append(elements[:])
                return  
            
            for i in range(num,n+1):
                elements.append(i)
                dfs(elements,i+1,length-1)
                elements.pop()
        result = [] 
        dfs([],1,k)
        return result