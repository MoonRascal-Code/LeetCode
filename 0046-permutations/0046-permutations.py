class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])
            
            for i in elements:
                next_elements = elements[:]
                next_elements.remove(i)
                
                prev_elements.append(i)
                dfs(next_elements)
                prev_elements.pop()
        
        result = [] 
        prev_elements = [] 
        dfs(nums)
        return result
