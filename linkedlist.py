class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return 

        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode

    def printList(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next


list = LinkedList()
list.head = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")
e4 = Node("Thursday")
e5 = Node("Friday")
e6 = Node("Saturday")
list.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
list.AtEnd("Sunday")
list.printList()
