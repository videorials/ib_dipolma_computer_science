from LinkedList import *
from ArrayList import *
from Solution import *

def main():
    
	# linked lists representing two positive integers in reverse order
    a1, a2 = [2,4,3], [5,6,4]
    l1, l2 = LinkedList(), LinkedList()
    for i in a1: l1.addFirst(i)
    for i in a2: l2.addFirst(i)

    solution = Solution()
    output = solution.addTwoNumbers(l1,l2)
    print(output.list())
	

if __name__ == "__main__":
    main()