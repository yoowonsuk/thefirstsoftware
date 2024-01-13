class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def printing(self):
        printvalue = self.head
        while printvalue is not None:
            print(printvalue.data)
            printvalue = printvalue.next

    def delNode(self,deldata):
        new = self.head
        if new is not None:
            if new.data == deldata:
                self.head = new.next
                new = None
                return
                
        while new is not None:
            if new.data == deldata:
                break
            prev = new
            new = new.next

        if new == None:
            return

        prev.next = new.next
        new = None

x = LinkedList()
x.head = Node("Umair")
data2 = Node("Bilal")
data3 = Node("Khan")
data4 = Node("Udemy")

x.head.next = data2
data2.next = data3
data3.next = data4

x.delNode("Khan")
x.printing()

