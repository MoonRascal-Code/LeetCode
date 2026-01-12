class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(elements,ind,k):
            # 종료 및 백트랙킹 
            if k == 0:
                result.append(elements[:])
                return 
            
            for i in range(ind,n+1):
                elements.append(i)
                dfs(elements,i+1,k-1)
                elements.pop()
        dfs([],1,k)
        return result

# return list(itertools.combinations(range(1,n+1),k))