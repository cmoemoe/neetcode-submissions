# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        N = 0
        while tmp:
            N+=1
            tmp = tmp.next

        removeIdx = N - n
        if removeIdx == 0:
            return head.next
        
        cur = head
        for i in range(N-1):
            if (i+1) == removeIdx:
                cur.next = cur.next.next
                break
            cur = cur.next
            
        return head
        
