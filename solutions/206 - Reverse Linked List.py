# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous_ptr = None
        current_ptr = head

        while current_ptr is not None:
            temp = current_ptr.next
            current_ptr.next = previous_ptr
            previous_ptr = current_ptr
            current_ptr = temp
        head = previous_ptr
        return head
