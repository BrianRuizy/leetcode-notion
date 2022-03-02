# 21 - Merge Two Sorted Lists

Difficulty: easy
Done: Yes
Last edited: March 2, 2022 1:53 AM
Link: https://leetcode.com/problems/merge-two-sorted-lists/submissions/
Topic: linked list

## Problem

---

You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists in a one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

![Untitled](images/21-2.png)

## Solution

---

Solution can be done in a single iterative traversal, resulting in linear time complexity. To do so we would need to traverse both lists with the use of a pointer —*previous—* which essentially tracks the current place in the final list. 

Additionally we would need to add a sentinel node (hypothetical first node). This allows to functionally make the final merged list never empty.

The while loop —typical for linked list problems— only runs while l1 or l2 do not point to None. Since 

## Whiteboard

---

![Untitled](images/21-1.png)

## Code

---

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        
        # the while loop only runs while l1 or l2 are not None
        
        # since lists can be diffent sizes,
        # when we've reached the end for one we can point
        # the merged list to the non-null list
        previous.next = list1 or list2
        
        return s.next
```

## Time Complexity

---

big O