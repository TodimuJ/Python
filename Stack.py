class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop(0)

    def print_stack(self):
        print(self.items)

class Queue:
    def __init__(self):
        self.items = []
        

s = Stack()
s.push(20)
s.push(23)
s.push(0)
s.push(40)
s.push(276)
s.print_stack()
s.pop()
s.print_stack()
    
