# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0 
        def dfs(node:TreeNode):
            if node is None:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest,left+right+2) # 거리값, 최대 길이 
            # 왼쪽 부터 오른쪽 reaf노드 까지의 거리 
            return max(left,right)+1 # 상태 값 

        dfs(root)        
        return self.longest
