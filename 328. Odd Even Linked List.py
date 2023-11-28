# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next==None:
            return head
        odd = head
        even = head.next
        link_even = even
        while odd!=None and even!=None and even.next!=None and odd.next!=None :
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = link_even
        return head
