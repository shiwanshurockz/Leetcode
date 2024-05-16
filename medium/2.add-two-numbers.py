# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        counter1 = l1
        counter2 = l2
        counter3 = ListNode(None,None)
        res = counter3
        rem = 0
        while counter1 is not None and counter2 is not None:
            temp = counter1.val + counter2.val + rem
            rem = temp // 10
            newNode = ListNode(temp % 10,None)
            counter3.next = newNode

            counter3 = counter3.next
            counter1 = counter1.next
            counter2 = counter2.next
        while counter1 is not None:
            temp = counter1.val + rem
            rem = temp // 10
            newNode = ListNode(temp % 10,None)
            counter3.next = newNode

            counter3 = counter3.next
            counter1 = counter1.next
        while counter2 is not None:
            temp = counter2.val + rem
            rem = temp // 10
            newNode = ListNode(temp % 10,None)
            counter3.next = newNode

            counter3 = counter3.next
            counter2 = counter2.next
        if rem is not 0:
            newNode = ListNode(rem,None)
            counter3.next = newNode

        return res.next
        
