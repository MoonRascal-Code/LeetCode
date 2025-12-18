# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # =========== 파이썬 다운 방식 =========== 
        # if root:
        #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        #     return root 
        # return None

        # =========== BFS =========== 
        # q = collections.deque([root])

        # while q:
        #     node = q.popleft()

        #     if node:
        #         node.left, node.right = node.right, node.left
        #         q.append(node.left)
        #         q.append(node.right)

        # return root
        # =========== DFS =========== 
        s = collections.deque([root])

        while s:
            node = s.pop()
            
            if node:
                node.left, node.right = node.right, node.left
                s.append(node.left)
                s.append(node.right)
        return root 