from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q, lock):
    while True:
        value = q.get() #gets and remove the value from queue
        
        with lock:      # prevent printing at the same time with this lock (prevents printing in the same line)
            print(f"thread: {current_thread().name} got {value}")

        #For each get(), a subsequent call to task_done() tells the queue that the processing on this item is complete.
        # If all tasks are done, q.join() can unblock
        q.task_done() 

if __name__ == "__main__":
    q = Queue()
    num_threads = 5
    lock = Lock()

    for i in range (num_threads):
        thread = Thread(target=worker, args=(q,lock))
        thread.daemon = True #it is False by default        # dies when the main thread dies
        thread.start()

    #adding values to the queue
    for x in range(30):
        q.put(x)

    q.join()    #blocks until all the items in the queue have been got and printed

    print("end main")