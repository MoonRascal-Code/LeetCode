# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.result = 0 
        def dfs(node:TreeNode):
            if node is None:
                return 0 
            
            left = dfs(node.left)
            right = dfs(node.right)

            # 같은 요소의 길이를 구하는 식 
            if node.left and node.left.val == node.val:
                left +=1
            else:
                left = 0 
            
            if node.right and node.right.val == node.val:
                right +=1 
            else: 
                right =0

            self.result = max(self.result,left+right)
            return max(left,right) # 큰 쪽으로만 가면 됨
        dfs(root)
        return self.result 
        