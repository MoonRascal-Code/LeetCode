class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i,v in enumerate(nums):
            table[v] = i 
        
        for i,v in enumerate(nums):
            another = target - v
            if another in table and table[another] != i:
                return [i,table[another]]
