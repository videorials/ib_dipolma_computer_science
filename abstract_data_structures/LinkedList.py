# IB Assessment Statement | Methods that should be known are:
    # add (head and tail), insert (in order), delete, list, isEmpty, isFull.

# IB Java Examination Subset Tool (JETS) | based on https://docs.oracle.com/javase/7/docs/api/java/util/LinkedList.html
    # LinkedList<E> where E defines the type of elements held in the list
    # add(E e), addFirst(E e), addLast(E e)
    # clear()
    # element(), get(int index), getFirst(), getLast()
    # remove(), remove(int index), removeFirst(), removeLast()
    # size()
    # isEmpty()

# https://youtu.be/qp8u-frRAnU
# https://www.cs-ib.net/sections/05-05-linked-lists.html

class Node:

    # >> ----------------------------------------------------------------------------- >> constructor method <<
    def __init__ (self, data, next=None):

        self.data = data
        self.next = next
    
    # >> ----------------------------------------------------------------------------- >> setter methods <<

    def setNext(self, element):
        self.next = element

    # >> ----------------------------------------------------------------------------- >> getter methods <<

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next


class LinkedList:

    # >> ----------------------------------------------------------------------------- >> constructor method <<
    def __init__(self):
        self.head = None

    # >> ----------------------------------------------------------------------------- >> setter methods <<
    
    def addFirst(self, element):
        # >> -------------------- >> inserts element at beginning (head) of list
        self.head = Node(element, self.head)

    def addLast(self, element):
        # >> -------------------- >> appends element to end (tail) of list
        if self.head == None:
            self.head = Node(element, None)
        else:
            node_iterator = self.head
            while node_iterator.getNext() != None:
                node_iterator = node_iterator.getNext()
            node_iterator.setNext(Node(element, None))

    def removeFirst(self):
        # >> -------------------- >> removes and returns first element from list
        if self.head == None:
            return
        else:
            data = self.head.getData()
            self.head = self.head.getNext()
            return data

    def removeLast(self):
        # >> -------------------- >> removes and returns last element from list
        node_iterator = self.head

        while node_iterator.getNext().getNext() != None:
            node_iterator = node_iterator.getNext()
        
        data = node_iterator.getNext().getData()
        node_iterator.setNext(None)
        return data

    def clear(self):
        # >> -------------------- >> Removes and returns all elements from list
        data = self.list()
        self.head = None
        return data

    # >> ----------------------------------------------------------------------------- >> getter methods <<

    def getFirst(self):
        # >> -------------------- >> returns first element in list
        return self.head.getData()

    def getLast(self):
        # >> -------------------- >> returns last element in list
        node_iterator = self.head

        while node_iterator.getNext() != None:
            node_iterator = node_iterator.getNext()

        return node_iterator.getData()

    def list(self):
        # >> -------------------- >> returns string containing elements in list (in order), if present
        if self.isEmpty():
            return ("List is empty")
        else:
            node_iterator = self.head
            list_as_string = ''
            while node_iterator != None:
                list_as_string += str(node_iterator.getData())
                if node_iterator.getNext() != None:
                    list_as_string += ' --> '
                node_iterator = node_iterator.getNext()
            return list_as_string

    def size(self):
        # >> -------------------- >> returns number of elements in list
        node_iterator = self.head
        count_nodes = 0

        while node_iterator != None:
            count_nodes += 1
            node_iterator = node_iterator.getNext()

        return count_nodes

    def isEmpty(self):
    # >> -------------------- >> returns true if list contains no elements, false otherwise
        if self.head == None:
            return True
        else:
            return False


class Queue(LinkedList):

    def enqueue(self, element):
        self.addLast(element)
    
    def dequeue(self):
        self.removeFirst()
            

class Stack(LinkedList):

    def push(self, element):
        self.addFirst(element)
    
    def pop(self):
        self.removeFirst()
