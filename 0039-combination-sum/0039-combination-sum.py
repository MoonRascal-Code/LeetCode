class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = [] 
        def dfs(elements,ind):
            # backtracking 
            if target < sum(elements):
                return 

            elif target == sum(elements):
                result.append(elements[:])
                return 
            
            for i in range(ind,len(candidates)):
                elements.append(candidates[i])
                dfs(elements,i)
                elements.pop()
        dfs([],0)
        return result
