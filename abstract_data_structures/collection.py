class List:
    def __init__(self):
        self.list = []
    
    def add(self, value):
        self.list.append(value)
    
    def delete(self, value):
        if not self.is_empty():
            for i in range(len(self.list)):
                if value == self.list[i]:
                    self.list.pop(i)
                    break
        return None

    def traverse(self):
        if not self.is_empty():
            for i in self.list:
                print(i)

    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.insert(0, item)
        return None
    
    def dequeue(self):
        if not self.is_empty():
            self.queue.pop()
        return None
    
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    
    def front(self):
        return self.queue[-1]
    
    def back(self):
        return self.queue[0]

class Stack:
	def __init__(self):
		self.stack = []
	
	def push(self, item):
		self.stack.append(item)
		return None
	
	def pop(self):
		if not self.is_empty():
			self.stack.pop()
		return None
	
	def is_empty(self):
		if len(self.stack) == 0:
			return True
		else:
			return False
	
	def peek(self):
		if not self.is_empty():
			return self.stack[-1]
		return None
