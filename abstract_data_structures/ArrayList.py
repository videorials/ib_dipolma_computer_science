# IB Java Examination Subset Tool (JETS) | based on https://docs.oracle.com/javase/7/docs/api/java/util/ArrayList.html

class ArrayList:

    # >> ----------------------------------------------------------------------------- >> constructor method <<
    def __init__(self):
        self.arrayList = []

    # >> ----------------------------------------------------------------------------- >> setter methods <<
    
    def addFirst(self, element):
        # >> -------------------- >> inserts element at beginning (head) of list
        self.arrayList.insert(0, element)

    def addLast(self, element):
        # >> -------------------- >> appends element to end (tail) of list
        self.arrayList.append(element)

    def removeFirst(self):
        # >> -------------------- >> removes and returns first element from list
        if not self.isEmpty():
            data = self.arrayList[0]
            self.arrayList.pop(0)
            return data

    def removeLast(self):
        # >> -------------------- >> removes and returns last element from list
        if not self.isEmpty():
            data = self.arrayList[-1]
            self.arrayList.pop()
            return data

    def clear(self):
        # >> -------------------- >> Removes and returns all elements from list
        data = self.list()
        self.arrayList = []
        return data

    # >> ----------------------------------------------------------------------------- >> getter methods <<

    def getFirst(self):
        # >> -------------------- >> returns first element in list
        if not self.isEmpty():
            return self.arrayList[0]

    def getLast(self):
        # >> -------------------- >> returns last element in list
        if not self.isEmpty():
            return self.arrayList[-1]

    def list(self):
        # >> -------------------- >> returns string containing elements in list (in order), if present
        if self.isEmpty():
            return ("List is empty")
        else:
            list_as_string = ''
            list_size = len(self.arrayList)
            for index in range(list_size):
                list_as_string += str(self.arrayList[index])
                if index < list_size - 1:
                    list_as_string += ' --> '
            return list_as_string

    def size(self):
        # >> -------------------- >> returns number of elements in list
        return len(self.arrayList)

    def isEmpty(self):
    # >> -------------------- >> returns true if list contains no elements, false otherwise
        if len(self.arrayList) == 0:
            return True
        else:
            return False


class Queue(ArrayList):

    def enqueue(self, element):
        self.addLast(element)
    
    def dequeue(self):
        self.removeFirst()
            

class Stack(ArrayList):

    def push(self, element):
        self.addFirst(element)
    
    def pop(self):
        self.removeFirst()
