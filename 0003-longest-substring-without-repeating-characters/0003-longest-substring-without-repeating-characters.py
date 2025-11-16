class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # tmmzuxt 
        max_length = 0 
        start = 0 
        used = dict() 
        for ind,char in enumerate(s):
            if char in used and start<= used[char]:
                start = used[char] + 1 
            else:
                max_length = max(max_length, ind-start+1)
            used[char] = ind 

        return max_length