# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0 
        def dfs(node):
            if not node: 
                return -1  # 존재하지 않은 노드에 -1 부여 
            
            left = dfs(node.left)  #2 / 4 5 / -1 -1 : -1 -1  
            right = dfs(node.right) 

            self.longest = max(self.longest, left+right+2)
            return max(left,right) +1 
            
        dfs(root)
        return self.longest
            