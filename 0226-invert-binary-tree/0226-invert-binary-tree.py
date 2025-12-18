# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 파이썬 다운 방식 
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root 
        return None
        # BFS
        # DFS 