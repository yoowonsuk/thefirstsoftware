class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
    def add(self, value):
        a = Node(value)
        a.next = self.head
        if self.head is not None:
            self.head.prev = a
        self.head = a
    
    def printing(self,node):
        while(node is not None):
            print(node.data)
            last = node
            node = node.next

x = LinkedList()
x.add("Umair")
x.add("Bilal")
x.add("khan")
x.add("Udemy")
x.printing(x.head)
