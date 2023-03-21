class ArrayList:
    def __init__(self, size=None):
        self.container = []
        self.fixed_size = size
    
    def set_fixed_size(self, size):
        self.fixed_size = size
    
    def get_fixed_size(self):
        return self.fixed_size
    
    def is_full(self):
        if self.get_fixed_size() != None:
            if len(self.container) == self.get_fixed_size():
                return True
        return False
    
    def is_empty(self):
        if len(self.container) == 0:
            return True
        return False

class Stack(ArrayList):
    def push(self, item):
        self.container.append(item)
    
    def pop(self):
        removed = None
        if not self.is_empty():
            removed = self.container[-1]
            self.container.pop()
        return removed

class Queue(ArrayList):
    def enqueue(self, item):
        self.container.append(item)
    
    def dequeue(self):
        removed = None
        if not self.is_empty():
            removed = self.container[0]
            self.container.pop(0)
        return removed
    
    def front(self):
        if not self.is_empty():
            return self.container[0]
        return None
    
    def back(self):
        if not self.is_empty():
            return self.container[-1]
        return None


