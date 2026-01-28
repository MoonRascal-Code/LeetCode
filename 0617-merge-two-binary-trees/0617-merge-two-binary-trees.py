# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(t1 , t2):
            if t1 and t2:
                t1.val+= t2.val 

                t1.left= dfs(t1.left, t2.left)
                t1.right = dfs(t1.right, t2.right)
                return t1

            else:
                return t1 or t2


        return dfs(root1, root2)