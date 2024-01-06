import re
def phonenumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
    


message = ("444-555-6789 is my uncle's phone abhijeetopop number")
for i in range(len(message)):
    chunk = message[i:i+12]
    if phonenumber(chunk):
        print("the number is: "+ chunk)
print("done")

