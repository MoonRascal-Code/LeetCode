# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoList(self,l1:ListNode,l2:ListNode)->ListNode:
        if l1 and l2:
            if l1.val>l2.val:
                l1,l2 = l2,l1
            l1.next = self.mergeTwoList(l1.next,l2)
        return l1 or l2 
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 병합정렬 
        if not (head and head.next):
            return head
        # 1. 중간 지점을 찾는다. (fast, slow)
        half, slow,fast = None, head,head 
        while fast and fast.next :
            half,slow, fast = slow,slow.next, fast.next.next
        half.next = None # slow랑 연결 끊는것 
        # 2. 중간을 기준으로 두 분류로 나눈다. 
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        # 3. 병합 정렬 
        # 4. 합친다. 
        return self.mergeTwoList(l1,l2)
