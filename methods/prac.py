# # def phonenumber(text):
# #     if len(text) != 12:
# #         return False
# #     for i in range(0,3):
# #         if not text[i].isdecimal():
# #             return False
# #     if text[3] != '-':
# #         return False
# #     for i in range(4,7):
# #         if not text[i].isdecimal():
# #             return False
# #     if text[7] != '-':
# #         return False
# #     for i in range(8,12):
# #         if not text[i].isdecimal():
# #             return False
# #     return True
    


# # message = ("444-555-6789 is my uncle's phone abhijeetopop number")
# # for i in range(len(message)):
# #     chunk = message[i:i+12]
# #     if phonenumber(chunk):
# #         print("the number is: "+ chunk)
# # print("done")

# import re

# phone = re.compile(r'\d{3}-\d{3}-\d{4}')

# text = ("this 444-555-6677 is my phone number")

# match = phone.search(text)

# # print("number is : "+match.group())
import re

# m = re.compile(r'batman|bruce banner')
# m1 = m.findall("i am bruce aswwll as batman & bruce banner ")
# m2 = m.findall("bruce banner and batman are the hero")
# print(m2)
m1 = re.compile(r'(bat(?:copter|mobile|car|man))')
text = ("batman has a cool batcar,batmobile & batcopter")
a = (re.findall(m1,text))
for i in a:
    print(i)