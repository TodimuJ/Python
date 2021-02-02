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

    def reverse(self):
        itr = self.head

        while(itr):
            self.insertAB(itr.data)
            itr = itr.next

        return itr


    
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
            llstr = ''
            
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
    lkdlst = LinkedList()
    lkdlst.insertAB(5)
    lkdlst.insertAB(16)
    lkdlst.insertAB(37)
    lkdlst.insertAB(19)
    lkdlst.insert(50)
    # lkdlst.insertValues(["mangoes", "oranges", "bananas", "grapes"])
    lkdlst.print()
    print(lkdlst.length())
    lkdlst.remove(3)
    lkdlst.print()
    lkdlst.insertAt(28, 0)
    lkdlst.print()
    lkdlst.insertAt(44, 3)
    lkdlst.print()
    lkdlst.insert(67)
    lkdlst.print()
    lkdlst.insertAt(100, 4)
    lkdlst.print()
    print(lkdlst.length())
    lkdlst.remove(2)
    lkdlst.print()
    print(lkdlst.length())
    lkdlst.reverse()
    lkdlst.print()
