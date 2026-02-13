# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder: # 자식 노드가 없을 경우 None 처리 
            middle = preorder.pop(0) # 3 , 9, 20
            ind = inorder.index(middle)

            node = TreeNode(middle) 
            node.left = self.buildTree(preorder, inorder[:ind]) # 9
            node.right = self.buildTree(preorder,inorder[ind+1:]) # 15,20,7 

            return node