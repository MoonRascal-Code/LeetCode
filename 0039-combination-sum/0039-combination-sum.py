class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = [] 
        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0: # 음수
                return 
            if csum == 0: # 정답인 경우 
                result.append(path)
                return 
            
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path+[candidates[i]])
            
        dfs(target,0,[])
        return result 