class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] 
        volume = 0 
        
        for ind,h in enumerate(height):
            while stack and height[stack[-1]] < h:
                prev_ind = stack.pop() 
                
                if not stack:
                    break 
                # 거리 
                s = ind - stack[-1] - 1 
                # 높이
                he = min(height[stack[-1]], h) - height[prev_ind]
                volume += s * he

            stack.append(ind)
        return volume