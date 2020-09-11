import sys


# implementation of queue data structure from scratch using list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class MinStack:
    def __init__(self):
        self.head = None

    def __repr__(self):
        # traverse stack and print all values
        curr = self.head
        nodes_list = []
        while curr:
            nodes_list.append(str(curr.data))
            curr = curr.next
        nodes_list.append('None')
        return ', '.join(nodes_list)

    def pop(self):
        # remove node from head
        current = self.head
        self.head = current.next
        current = None

    def push(self, x):
        # insert new node between head and first element in the list
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
        if self.head is None:
            return None

        minimum = sys.maxsize
        current = self.head
        while current is not None:
            if minimum > current.data:
                minimum = current.data
            current = current.next
        return minimum
