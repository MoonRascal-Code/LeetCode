class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # ind = bisect.bisect_left(nums,target)
        # if ind < len(nums) and nums[ind] == target:
        #     return ind
        # return -1 
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2 

            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                return mid
        return -1 