class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ind = bisect.bisect_left(nums,target)
        if ind < len(nums) and nums[ind] == target:
            return ind
        return -1 