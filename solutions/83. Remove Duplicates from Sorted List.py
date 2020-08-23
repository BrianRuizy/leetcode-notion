# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """Runner pointer traversal, passing node values to hashmap with unique keys. 
        If key already present --hence, unique-- 'delete' that node
        """
        previous = None
        current = head
        nodes_dict = {}

        while current is not None:
            if current.val not in nodes_dict:
                nodes_dict[current.val] = 1
                previous = current
            else:
                previous.next = current.next

            current = current.next

        return head
