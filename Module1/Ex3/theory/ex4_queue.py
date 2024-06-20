class MyQueue():
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.my_queue = []
        
    def is_empty(self):
        return len(self.my_queue) == 0
    
    def is_full(self):
        return len(self.my_queue) == self.capacity
    
    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            return
        self.my_queue.append(value)
        
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.my_queue.pop(0)
    
    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.my_queue[0]
    
if __name__ == "__main__":
    queue1 = MyQueue(5)
    queue1.enqueue(1)
    queue1.enqueue(2)
    print(queue1.is_full())
    
    print(queue1.front())
    
    print(queue1.dequeue())
    
    print(queue1.front())
    
    print(queue1.dequeue())
    
    print(queue1.is_empty())