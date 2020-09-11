# implementation of stack data structure from scratch using linkedlist
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
