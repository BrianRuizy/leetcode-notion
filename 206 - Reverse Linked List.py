# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """will reverse list iteratively,
        by traversing and flipping the next pointer of each node
        """
        previous_ptr = None  # previous pointer, initialized to null
        current_ptr = head  # current pointer, at head

        while current_ptr is not None:
            temp = current_ptr.next   # temp buffer, pointing to next node
            current_ptr.next = previous_ptr  # reverse link of current_ptr to prev
            previous_ptr = current_ptr  # ---- resume traversal ----
            current_ptr = temp
        head = previous_ptr
        return head
