import collection as collection

def main():
    
	new_queue = collection.Queue()
	new_queue.enqueue(29)
	new_queue.enqueue(66)
	new_queue.enqueue(13)
	print(new_queue.front())
	print(new_queue.back())
	new_queue.dequeue()
	print(new_queue.front())

if __name__ == "__main__":
    main()