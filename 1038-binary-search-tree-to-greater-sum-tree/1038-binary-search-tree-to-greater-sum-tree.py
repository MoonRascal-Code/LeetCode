# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = 0
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            # 중위 순회 
            # 오른쪽 부터 재귀로 맨 밑에서 부터 계산 
            self.bstToGst(root.right)
            self.val += root.val # 현재 값 계산 
            root.val = self.val # 값 변경 
            self.bstToGst(root.left) # 왼쪽 순회 

        return root 
