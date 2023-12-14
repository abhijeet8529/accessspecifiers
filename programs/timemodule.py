import time


# def usingfor():

#     for i in range(100000):
#         print(i)
# ? time.time() in timemodule

# def usingwhile():
#     i = 0
#     while i < 100000:
#         i = i+1
#         print(i)


# ex = time.time()
# usingfor()
# a = time.time() - ex
# usingwhile()
# b = time.time() - ex
# print(a)
# print(b)


# print("time")
# time.sleep(3)                            #? time.sleep()
# print("vedya this printed is after 3 seconds")

t = time.localtime()
ft = time.strftime("%Y-%m-%d & %H:%M:%S", t)
print(ft)
