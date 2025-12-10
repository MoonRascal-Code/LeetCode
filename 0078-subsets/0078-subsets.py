class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 

        def dfs(index,prev):
            res.append(prev)
            if len(prev) == len(nums):
                return 
            

            for ind in range(index,len(nums)):
                dfs(ind+1,prev+[nums[ind]])

        dfs(0,[])
        return res
