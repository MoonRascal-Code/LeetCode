class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [] 
        path = [] # 현재 선택한 숫자들 

        def dfs(start):
            if len(path) == k:
                res.append(path[:])
                return 

            for char in range(start,n+1):
                path.append(char) # 선택 
                dfs(char+1) # 다음 선택 // 놓친 부분 
                path.pop() # 백트래킹 // 놓친 부분 
        dfs(1)

        return res
