class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        @staticmethod
        def to_swap(n1:int, n2:int) -> bool:
            return str(n1) + str(n2) < str(n2) + str(n1)
        
        i = 1
        while i < len(nums):
            j = i 
            while j > 0 and to_swap(nums[j-1],nums[j]):
                nums[j], nums[j-1] = nums[j-1],nums[j] # 스왑
                j-=1 
            i+=1 
        return str(int(''.join(map(str,nums)))) # '00' 때문에