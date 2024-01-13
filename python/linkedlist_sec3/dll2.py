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

    def printing(self,node):
        while(node is not None):
            print(node.data)
            last = node
            node = node.next
    def remove(self, node):
        if node.prev is None:
            self.head = node.next
            #self.x = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            pass #self.y = node.prev
        else:
            node.next.prev = node.prev

x = LinkedList()
x.add(2)
x.add(3)
x.add(4)
x.add(5)
#x.remove(x.head.next)
#x.remove(x.head)
x.remove(x.head.next.next.next)
x.printing(x.head)
