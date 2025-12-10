class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = [] 
        res = [] 
        
        def dfs(start):
            ele_sum = sum(path)
            if target < ele_sum:
                return 

            elif target == ele_sum:
                res.append(path[:])
                return 
        
            # for c in candidates: # 조합이기 때문에 
            for ind in range(start,len(candidates)):
                path.append(candidates[ind])
                dfs(ind)
                path.pop()

        dfs(0)
        return res