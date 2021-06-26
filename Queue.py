class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enque(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) < 1:
            return None
        return self.items.pop()

    def print_stack(self):
        print(self.items)

    def size(self):
        return len(self.items)

q = Queue()
q.enque(2)
q.enque(1)
q.enque(4)
q.enque(45)
q.enque(76)
q.enque(30)
print(q.size())
q.print_stack()
q.dequeue()
print(q.size())
q.print_stack()
print(q.isEmpty())
