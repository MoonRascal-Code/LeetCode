# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])

        while queue:
            cur = queue.popleft()
            if cur is not None:
                cur.left, cur.right = cur.right, cur.left

                queue.append(cur.left)
                queue.append(cur.right)

        return root