# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        Dummy = ListNode(0,head)
        groupPrev = Dummy

        while True:
            kth = self.getKthNode(groupPrev,k)
            if kth is None:
                break
            kthNext = kth.next
            prev = kthNext
            curr = groupPrev.next
            while curr != kthNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return Dummy.next

    
    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
