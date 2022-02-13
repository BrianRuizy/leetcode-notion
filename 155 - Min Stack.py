# ------------------------------ 2nd optimal submission -----------------------
# Your runtime beats 98.90 % of python3 submission

# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Memory Usage: 17.6 MB

# using 2 stacks AND built-in pop(), append() methods, proved faster than
# implementing a linked list solution ??

class MinStack2:
    def __init__(self):
        self.stack = []
        self.smallest = [9223372036854775807]

    def pop(self):
        current = self.stack[-1]
        if current == self.smallest[-1]:
            self.smallest.pop()
        self.stack.pop()

    def push(self, x):
        if x <= self.smallest[-1]:
            self.smallest.append(x)
        self.stack.append(x)

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.smallest[-1]

# ------------------------------ 1st optimized submission ---------------------
# Your runtime beats 62.03 % of python3 submissions

# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 68 ms
# Memory Usage: 18.4 MB

# implementation of stack data-structure from scratch using linkedlist
# many solutions I seen use a regular [] list with built in pop(), append() methods


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class MinStack:
    def __init__(self):
        self.head = None
        self.smallest = [9223372036854775807]

    def pop(self):
        # remove node from head
        current = self.head
        if current.data == self.smallest[-1]:
            self.smallest.pop()
        self.head = current.next
        current = None

    def push(self, x):
        # insert new node between head and first element in the list
        # keep track of the smallest number being pushed into the list
        if x <= self.smallest[-1]:
            self.smallest.append(x)

        new_node = Node(data=x)  # initialize new node
        new_node.next = self.head
        self.head = new_node

    def top(self):
        try:
            top = self.head.data
        except AttributeError:
            top = 'Stack is empty'
        return top

    def getMin(self):
        return self.smallest[-1]
