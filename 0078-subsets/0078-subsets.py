class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index,path):
            if path == len(nums):
                return 
            result.append(path)

            for i in range(index,len(nums)):
                dfs(i+1,path+[nums[i]]) # 0 , [1] / 0, [1,2], / [1,2,3] / [1,3]

        result = [] 
        dfs(0,[])
        return result 
