# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        upper = 0 
        l3 = prev = ListNode(None)

        while l1 is not None or l2 is not None:
            l1_v = l1.val if l1 is not None else 0 
            l2_v = l2.val if l2 is not None else 0 

            print(l1_v,l2_v)
            pre = ((l1_v+l2_v+upper) % 10) 
            l3.next = ListNode(pre) 
            upper = (l1_v+l2_v+upper)// 10 

            l1 = l1.next if l1 is not None else l1 
            l2 = l2.next if l2 is not None else l2 
            l3 = l3.next
        if upper != 0 :
            l3.next = ListNode(upper) 
        return prev.next
        