# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #交換
        prev = None
        current = head
        while current:
            next_N = current.next#1.先斷方向線
            current.next = prev
            prev = current
            current = next_N
        return prev
