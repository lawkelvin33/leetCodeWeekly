# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        traversed = []
        while head!=None:
            if head in traversed:
                return head
            else:
                traversed.append(head)
                head = head.next
        return None