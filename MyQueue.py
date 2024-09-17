class MyQueue:
    def __init__(self):
        # Store elements
        self.data = []
        # Pointer to indicate the start position
        self.p_start = 0

    # Insert an element into the queue. Return True if the operation is successful.
    def enQueue(self, x):
        self.data.append(x)
        return True

    # Delete an element from the queue. Return True if the operation is successful.
    def deQueue(self):
        if self.isEmpty():
            return False
        self.p_start += 1
        return True

    # Get the front item from the queue.
    def Front(self):
        if self.isEmpty():
            return None
        return self.data[self.p_start]

    # Checks whether the queue is empty or not.
    def isEmpty(self):
        return self.p_start >= len(self.data)


# Main block to test the queue
if __name__ == "__main__":
    q = MyQueue()
    q.enQueue(5)
    q.enQueue(3)
    
    if not q.isEmpty():
        print(q.Front())  # Output: 5
    
    q.deQueue()
    
    if not q.isEmpty():
        print(q.Front())  # Output: 3
    
    q.deQueue()
    
    if not q.isEmpty():
        print(q.Front())
