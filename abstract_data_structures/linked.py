class Linked_list:
    def __init__(self):
        self.value = None
        self.head = None
        self.tail = None
        self.max_size = 10
        self.node_count = 0

    
    def add_head(self, node):
        self.head = node
    

    def add_tail(self, node):
        self.head = node
    

    def insert(self, node):
        # in order
        None
    

    def delete(self, node):
        None


    def list(self):
        # print out each value in list
        None
    

    def is_empty(self):
        if self.node_count == 0:
            return True
        else:
            return False
    

    def is_full(self):
        if self.node_count == self.max_size:
            return True
        else:
            return False