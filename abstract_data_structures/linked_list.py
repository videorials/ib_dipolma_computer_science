# https://youtu.be/qp8u-frRAnU
# https://www.cs-ib.net/sections/05-05-linked-lists.html

# Methods | add (head and tail), insert (in order), delete, list, isEmpty, isFull.

class Node:
    # -------------------- >> constructor method <<
    def __init__ (self, data=None, next=None):
        '''
        >> The default value of None is assigned to instance variables head and next, which
           store the data and pointer Node (or None), respectively.
        '''
        self.data = data
        self.next = next

class LinkedList:
    # >> -------------------- >> constructor method <<
    def __init__(self, head=None):
        '''
        >> The default value None is assigned to the instance variable head, which stores
           the Node at the head of the LinkedList.
        '''
        self.head = head

    # >> -------------------- >> setter methods <<
    def insert_at_head(self, data):
        '''
        >> An instance of class Node is instantiated, using the data passed in and the
           current value of the instance variable head (either a Node or None), which is
           then assigned to the instance variable head, thus replacing it with the new Node.
        '''
        self.head = Node(data, self.head)
    
    def insert_at_tail(self, data):
        '''
        >> IF the LinkedList is empty... a new Node is instantiated, using the data passed
           in and the value None. This is then assigned to the instance variable head.
        >> ELSE... the Node stored in the instance variable head is assigned to a temporary
           variable node_iterator. While the value stored in node_iterator is a Node (i.e. not None),
           the next instance variable, of the Node currently stored in node_iterator, is assigned
           to node_iterator.
        >> When the last Node in the LinkedList is reached... a new Node is instantiated, using
           the data passed in and the value None. This is then assigned to the next instance variable
           of the Node currently stored in node_iterator.
        '''
        if self.head == None:
            self.head = Node(data, None)
            return
        else:
            node_iterator = self.head
            while node_iterator.next != None:
                node_iterator = node_iterator.next
            node_iterator.next = Node(data, None)

    def insert_values(self, data_list):
        '''
            None is assigned to the instance variable head, which effectively empties the LinkedList.

            Iterate through the data list, feeding each data item into the insert_at_tail method, thus adding
            each item to the tail of the LinkedList.
        '''
        self.head = None
        for data in data_list:
            self.insert_at_tail(data)

    def insert_at(self, data):
        '''
        >> Add comments here...
        '''
        None
    
    def insert_after_value(self, data):
        '''
        >> Add comments here...
        '''
        None

    def remove_at(self, index):
        '''
        >> IF the index is outside acceptible range throw exception.
        >> ELSE IF index is zero, remove first element... adjusting head to next Node or None.
        >> ELSE traverse the LinkedList up to the Node before the index (one before)...
           > remove the next element... assign next next element to head.
        '''
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        elif index == 0:
            self.head = self.head.next
            return
        else:
            node_iterator = self.head
            count_nodes = 0
            while node_iterator != None:
                if count_nodes == index - 1:
                    node_iterator.next = node_iterator.next.next
                    return
                else: 
                    count_nodes += 1
                    node_iterator = node_iterator.next

    def remove_by_value(self, data):
        '''
            Add comments here...
        '''
        None

    # >> ------------------------------ >> getter methods <<

    def is_empty(self):
        
        if self.head == None:
            return True
        else:
            return False

    def print(self):
        '''
        >> IF the LinkedList is empty print appropriate message...
        >> ELSE iterate through each Node in the LinkedList, adding the data element of each Node to
           a string as you go...
        '''
        if self.is_empty():
            print("Linked list is empty")
        else:
            node_iterator = self.head
            list_as_string = ''
            while node_iterator != None:
                list_as_string += str(node_iterator.data) + ' --> '
                node_iterator = node_iterator.next
            print(list_as_string)

    def get_length(self):
        '''
        >> Iterate through each node in the LinkedList, incrementing a count variable as you go...
        '''
        node_iterator = self.head
        count_nodes = 0

        while node_iterator != None:
            count_nodes += 1
            node_iterator = node_iterator.next

        return count_nodes



ll = LinkedList()
# ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
# ll.print()
# ll.remove_at(2)
ll.print()