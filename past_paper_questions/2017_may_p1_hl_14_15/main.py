from linear_structures import *

def main():
    stack = Stack(10)
    queue = Queue(5)

    for i in range(1, stack.get_fixed_size() + 1):
        stack.push(i)

    queue.set_fixed_size(2)
    
    while not queue.is_full():
        queue.enqueue(stack.pop())
    
    print(stack.container)
    print(queue.container)

if __name__ == "__main__":
    main()
