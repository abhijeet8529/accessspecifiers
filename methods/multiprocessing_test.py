from multiprocessing import Process , freeze_support
import requests
import concurrent.futures


def down(url, name):
    print("started downloading")
    response = requests.get(url)
    open(f"files/file{name}.jpg ","wb").write(response.content)
    print("finished downloading")

    
url = "https://picsum.photos/2000/3000"

# for i in range(50):
    # l = []
#     # down(url , i)
#     if __name__ == '__main__':        #? multiprocessing
#         freeze_support()
#         a = Process(target=down, args=[url, i])
#         a.start()
#         l.append(a)
    
# for a in l:
#     a.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
    if __name__ == "__main__":
        l1 = [url for i in range(60)]         #? multithreading
        l2 = [i for i in range(60)]
        a = executor.map(down, l1 ,l2)
        for t in a:
            print(a)
        