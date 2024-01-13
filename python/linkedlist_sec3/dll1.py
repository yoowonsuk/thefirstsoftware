class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        new = Node(val)
        new.next = self.head
        if self.head is not None:
            self.head.prev = new
        self.head = new


    def insertion(self, node, value):
        new = Node(value)
        new.next = node.next
        node.next = new
        new.prev = node
        if new.next is not None:
            new.next.prev = new

    def appending(self, value):
        new = Node(value)
        new.next = None
        if self.head is None:
            new.prev = None
            self.head = new
            return
        
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
        pointer.next = new
        new.prev = pointer
        return

    def printing(self,node):
        while(node is not None):
            print(node.data)
            last = node
            node = node.next

x = LinkedList()
x.add(2)
x.add(5)
x.add(7)
x.add(9)
x.insertion(x.head.next, 12)
x.appending(20)
x.printing(x.head)
