# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or not lists:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]
    
    def mergeList(self, arr1,arr2):
        head = ListNode()
        tail = head

        while arr1 and arr2:
            if arr1.val < arr2.val:
                tail.next = arr1
                arr1 = arr1.next
            else:
                tail.next = arr2
                arr2 = arr2.next
            tail = tail.next
        if arr1:
            tail.next = arr1
        if arr2:
            tail.next = arr2
        return head.next
