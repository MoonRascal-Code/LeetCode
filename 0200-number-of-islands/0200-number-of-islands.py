class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            # 땅이 아닌 경우 
            if r < 0 or r >= len(grid) or \
                c < 0 or c >= len(grid[0]) or grid[r][c] != '1':
                return 
            
            # 땅 
            grid[r][c] = '#' # 가지치기
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        count = 0 
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count +=1
        return count 
