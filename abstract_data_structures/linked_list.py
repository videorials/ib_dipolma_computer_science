# https://youtu.be/qp8u-frRAnU
# https://www.cs-ib.net/sections/05-05-linked-lists.html

class Node:
    def __init__ (self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        # Create new instance of class Node, using data parameter provided, and the current value
        # of the head attribute, as parameters. Assign this new instance to head attribute.
        self.head = Node(data, self.head)
    
    def print(self):
        # If the linked list is empty print a message thus, if not...
        if self.head == None:
            print("Linked list is empty")
        else:
            # assign copy of head attribute (node instance) and empty string to two temporary variables...
            node_iterator = self.head
            list_as_string = ''

            # iterate while node_iterator variable a Node instance, i.e. not None
            while node_iterator != None:
                # concatenate Node's data attribute to list_as_string variable...
                list_as_string += str(node_iterator.data) + ' --> '
                # assign Node's next attribute to node_iterator variable
                node_iterator = node_iterator.next
            
            # print string containing node data to command line
            print(list_as_string)




ll = LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(89)
ll.print()