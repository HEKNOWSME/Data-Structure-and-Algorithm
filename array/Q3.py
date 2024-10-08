from collections import deque
stock_prices = [100.5, 107.3, 109.2, 111.1, 109.4, 107.0, 106.9]
maximum = 0
for price in stock_prices:
       if price > maximum:
              maximum = price
minimum = min(stock_prices)             
print('maximum', maximum)
print('minimum', minimum)

class Stack:
       def __init__(self):
              self.stack = deque()
       def push(self, item):
              self.stack.append(item)
              print(self.stack)
       def pop(self):
              if not self.stack:
                     raise IndexError('It is empty')
              self.stack.pop()
              print(self.stack)
       def peek(self):
              print(self.stack[len(self.stack) - 1])
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.peek()

class Queue:
       def __init__(self):
              self.items = deque()
       def enqueue(self,item):
              self.items.append(item)
              print(self.items)
       def dequeue(self):
              if not self.items:
                     raise IndexError('Nothing to remove')
              self.items.popleft()
              print(self.items)
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()