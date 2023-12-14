import time
import threading
from concurrent.futures import ThreadPoolExecutor

def func(sec):
    print(f"it takes around {sec} seconds to run")
    time.sleep(sec)
    return sec
    


# func(2)
# func(3)
# func(4)
def main():
    b1 = time.perf_counter()
    a1 = threading.Thread(target=func , args = [2])
    a2 = threading.Thread(target=func , args = [3])
    a3 = threading.Thread(target=func , args =[4])

    a1.start()
    a2.start()
    a3.start()

    a1.join()
    a2.join()
    a3.join()
    b2 = time.perf_counter()
    print(b1 - b2)

def poolingdemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 3)
        # print(future1.result())
        # future2 = executor.submit(func, 2)
        # print(future2.result())
        # future3 = executor.submit(func, 4)
        # print(future3.result())
        
        l = [1,2,4,5]
        results = executor.map(func, l)
        for result in results:
            print(result)    
poolingdemo()    