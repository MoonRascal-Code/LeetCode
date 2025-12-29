# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS 
        deque = collections.deque([root])

        while deque: 
            cur = deque.popleft() 

            if cur:
                cur.left, cur.right = cur.right, cur.left 

                deque.append(cur.left)
                deque.append(cur.right)

        return root 

