# Deque is a data structure that allows you to add and remove elements from both the front and the rear.
class Deque:
    def __init__(self):
        self.items = []

# isEmpty() checks if the deque is empty.
    def isEmpty(self):
        return self.items == []

# addRear() adds an element to the rear of the deque.
    def addRear(self, item):
        self.items.append(item)

# addFront() adds an element to the front of the deque.
    def addFront(self, item):
        self.items.insert(0, item)

# removeFront() removes an element from the front of the deque.
    def removeFront(self):
        return self.items.pop(0)

# removeRear() removes an element from the rear of the deque.
    def removeRear(self):
        return self.items.pop()

# size() returns the number of elements in the deque.
    def size(self):
        return len(self.items)

# Test the Deque class.
d = Deque()
print(d.isEmpty())
d.addRear(8)
d.addRear(5)
d.addFront(7)
d.addFront(10)
print(d.size())
print(d.isEmpty())
d.addRear(11)
print(d.removeRear())
print(d.removeFront())
d.addFront(55)
d.addRear(45)
print(d.items)