import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number : {i}")
    
def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Number : {letter}")

## Create 2 threads
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)

t=time.time()
t1.start()
t2.start()
## Wait for the threads to complete
t1.join()
t2.join()

finish_time=time.time()-t
print(finish_time)