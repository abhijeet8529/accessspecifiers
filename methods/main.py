def search(list , n):
    i = 0
    while i < len(list):
        if list[i] == n:
            return True
        i = i + 1
    return False
           
list = [1,4,5,6,7,9]   
n = 9

if search(list , n):
    print("found")
else:
    print("not found")