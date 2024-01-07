class Node:
    def __init__(self, datavalue=None):
        self.datavalue=datavalue
        self.nextvalue=None

class LinkedList:
    def __init__(self):
        self.headvalue=None
    def printing(self):
        printvalue = self.headvalue
        while printvalue is not None:
            if(printvalue.datavalue=="Udemy"):
                print(printvalue.datavalue)
                printvalue = printvalue.nextvalue
            else:
                printvalue = printvalue.nextvalue
        

x = LinkedList()
x.headvalue = Node("Umair Khan")
data2 = Node("Bilal Khan")
data3 = Node("Udemy")

x.headvalue.nextvalue = data2
data2.nextvalue = data3
data3.nextvalue = None # duplicate

x.printing()
