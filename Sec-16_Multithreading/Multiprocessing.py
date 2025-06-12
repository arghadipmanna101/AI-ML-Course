import multiprocessing
import multiprocessing.process
import time

def square():
    for i in range (5):
        time.sleep(1)
        print(f"Squre : {i*i}")
        
def cube():
    for i in range (5):
        time.sleep(1.5)
        print(f"Cube : {i*i*i}")
if __name__=="__main__":

    ## Create 2 processes
    t1= multiprocessing.Process(target=square)
    t2= multiprocessing.Process(target=cube)

    t=time.time()
    t1.start()
    t2.start()
    ## Wait for the threads to complete
    t1.join()
    t2.join()

    finish_time=time.time()-t
    print(finish_time)