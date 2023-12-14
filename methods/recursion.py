lesson = "my name is {} and im from country {}"
country = "india"
name = "abhijeet"
# print(lesson.format (name,country))
print(f"my name is {name} and im from {country}")

# # #...................above code fstring...................

n = int(input("enter the number : "))
f = int(input("enter the number :"))
print(f"the final number is :{  n*f }")
# #fstring...........................................................

# def s(n):
#     print(n+n)
# s (20)

# # #above code for sum ........................................


def math(n):
    if n == 0 or n == 1:
        return n
    else:
        return math(n - 1) + math(n - 2)


print(math(6))

# # #above code fibonchhi code ...................................

def facto(n):
    '''this is used for factoring'''
    if (n==0 or n ==1):
        return 1
    else:
        return n * facto(n - 1)
print(facto.__doc__)
print(facto(3))

# # #above code for docstring................


def multi(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)


print(multi(8))

# #above code for multiplying tables ................................

# def fibonachhi(n):
#     if (n==0 or n==1):
#         return n
#     else:
#         return (fibonachhi(n-1)+fibonachhi(n-2))
# print(fibonachhi(5))
# #above code fibonacchi ....................................
