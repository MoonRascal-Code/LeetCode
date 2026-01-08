class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            # back-tracking 
            if i < 0 or i>=len(grid) or \
                j < 0 or j >= len(grid[0]) \
                or grid[i][j] != "1":
                return 
            # "1" / 섬일 경우
            grid[i][j] = "#"
            # 상하좌우 추가 탐색 
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        island_count = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # back-traking 
                if grid[i][j] == "1":
                    dfs(i,j)
                    island_count +=1 
        return island_count 
