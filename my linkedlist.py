class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def append_to_head(self, data):
        # O(1) constant time, as inserting only interacts with head
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def append_to_tail(self, data):
        # adds node with value data to tail of LinkedList
        node = Node(data)
        if self.head is not None:
            self.head.next = node
            self.head = node
        else:
            self.tail

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def remove_node(self, target):
        current = self.head
        previous = None
        while current is not None:
            if current.get_data() == target:
                if previous:
                    previous.set_next(current.get_next())
                else:
                    self.head = current.get_next()
                return True
            previous = current
            current = current.get_next()
        return False
