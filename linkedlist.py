class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
 
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        NewNode = Node(data, None)
        if self.head is None:
            self.head = NewNode
            return
        
        itr = self.head
        
        while(itr.next):
            itr = itr.next
        
        itr.next = NewNode
        
    def insertAB(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insertValues(self, data):
        self.head = None
        
        for i in data:
            self.insert(i)
    
    def length(self):
        count = 0 
        
        itr = self.head
        
        while(itr):
            count += 1
            itr = itr.next
        
        return count
    
    def insertAt(self, data, index):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        if index  == 0:
            self.insertAB(data)
            return
        
        count = 0
        
        itr = self.head
        
        while(itr):
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break
                
            
            itr = itr.next
            count += 1 
        
    def print(self):
        
        if self.head == None:
            print("Linked List is empty")
            return
        else:
            itr = self.head
            llstr = 'Length of list is: '
            
            while itr:
                llstr += str(itr.data)
                if itr.next != None:
                    llstr += ' --> '
                itr = itr.next
            
            print(llstr)
            
    def remove(self, index):
        if self.head is None:
            print("Linked List is empty")
            return
        
        if index > self.length() or index < 1:
            print("Invalid index")
            return
        
        if index == 0:
            self.head = self.head.next
            return
            
            
        count = 0
        
        itr = self.head

        while(itr):
            
            if count == index -1:
                itr.next = itr.next.next
                break
            
            count += 1
            itr = itr.next
            
  
            

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAB(5)
    ll.insertAB(16)
    ll.insertAB(37)
    ll.insertAB(19)
    ll.insert(50)
    # ll.insertValues(["mangoes", "oranges", "bananas", "grapes"])
    ll.print()
    print(ll.length())
    ll.remove(3)
    ll.print()
    ll.insertAt(28, 0)
    ll.print()
    ll.insertAt(44, 3)
    ll.print()
    ll.insert(67)
    ll.print()
    ll.insertAt(100, 4)
    ll.print()
    print(ll.length())
    ll.remove(2)
    ll.print()
    print(ll.length())
