import LinkedList as lnklst
import ArrayList as arrlst

def main():
    
	new_queue = lnklst.Queue()
	new_queue.enqueue(29)
	new_queue.enqueue(66)
	new_queue.enqueue(13)
	print(new_queue.getFirst())
	print(new_queue.getLast())

if __name__ == "__main__":
    main()