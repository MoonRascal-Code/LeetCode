class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        path = [] 
        def dfs(elements,path):
            if len(nums) == len(path):
                result.append(path)
                # path.pop()
                return
            
            for i in elements:
                next_elements = elements[:]
                next_elements.remove(i)
                dfs(next_elements,path+[i])

        dfs(nums,[])
        return result
    # return list(itertools.permutation(nums))