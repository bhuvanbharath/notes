from multiprocessing import Process, Value, Array, Lock
import time

def add_100(number,lock):
    for _ in range(100):
        time.sleep(0.1)
        with lock:
            number.value+=1

def add_100_array(numbers,lock):
    for _ in range(100):
        time.sleep(0.1)
        with lock:
            for i in range(len(numbers)):
                numbers[i]+=1

if __name__ == "__main__":
    
    shared_number = Value('i', 0)   #'i' for integer
    print("Start:", shared_number.value)

    shared_array = Array('i', [3, 5, 7, 1, 9])
    print('Start:', shared_array[:])

    lock = Lock()

    process1 = Process(target=add_100, args=(shared_number,lock))
    process2 = Process(target=add_100, args=(shared_number,lock))

    process3 = Process(target=add_100_array, args=(shared_array,lock))
    process4 = Process(target=add_100_array, args=(shared_array,lock))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print('end value: ', shared_number.value)
    print('end value: ', shared_array[:])
