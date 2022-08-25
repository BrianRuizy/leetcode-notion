from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # create sentinel node
        s = ListNode(0, None)
        previous = s
        
        while list1 is not None and list2 is not None:
            # compare value at l1 vs value at l2
            # whichever is smaller that's where we point previous, and step that list
            # essentially prev keeps track of the new list
            
            if list1.val <= list2.val:
                previous.next = list1
                list1 = list1.next
            else: 
                previous.next = list2
                list2 = list2.next
                
            previous = previous.next
        
        # the while loop only runs while l1 or lx2 are not None
        
        # since lists can be diffent sizes,
        # when we've reached the end for one we can point
        # the merged list to the non-null list
        previous.next = list1 or list2
        
        return s.next



l1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=None)))
l2 = ListNode(val=4, next=ListNode(val=5, next=None))

s = Solution()
s.mergeTwoLists(list1=l1, list2=l2)