class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = [] 
        count = 0
        while head.next:
            list.append(head.val)
            head = head.next

        list.append(head.val)#還有最後一個

        for i in range(len(list)//2):
            if list[i] != list[-1-i]:
                count += 1
        if count != 0:
            return False
        else:
            return True
