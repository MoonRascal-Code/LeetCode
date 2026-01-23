class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: # 빼먹은 부분 
            return [] 

        graph = {'2': 'abc', '3':'def', '4':'ghi',
                    '5':'jkl','6':'mno','7':'pqrs',
                    '8':'tuv','9':'wxyz'}
        
        result = [] 
        def dfs(index, path):
            if len(digits) == len(path):
                result.append(path)
                return 
            
            for i in range(index,len(digits)):
                for j in graph[digits[i]]:
                    # dfs(index+1,path+j)
                    dfs(i+1,path+j)
        
        dfs(0,"")
        return result 

        