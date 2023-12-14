# multi = int(input("enter the number for muultiplication table : "))
# print(f"multiplication of the {multi} tables is : ")
# try:
#     for i in range(1, 11):
#         print(f"{int(multi)} x {i} = {int(multi) * i}")
#         if multi == 0:
#             print("MATHS NHI ATA KYA BE ???? ???")
#             break


# # except ValueError:
# #     print("your input is not a number\n have a nice day!!!!")

# # word = str(input("enter the word :"))


# # def change(a, b):
# #     try:
# #         for i in word:
# #             print(word.replace(a, b))
# #             break

# #         else:
# #             print("invalid input")

# #     except ValueError:
# #         print("current input is number not string")


# # change(a=input("enter to change : "), b=input("for what : "))

# # try:
# #     l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #     i = int(input("enter to index :"))
# #     print(len[i])
# # except:
# #     print("invalid input")

# # finally:
# #     print("im always executed")
# # n = input("Enter An Integer : ")
# # if n == "quit":
# #     print("OK!")
# # elif int(n) >= 5 and int(n) <= 9:
# #     print(f"Your Lucky Number Is : {int(n)*3 + 27}")
# # else:
# #     raise ValueError("LOMAD!, you entered invalid input.")
# import random as ran
# import string

# letters = string.ascii_lowercase
# st = input("enter to code : ")
# words = st.split(" ")
# coding = input("Enter your choice 0 or 1 :")
# coding = True if (coding == "1") else False
# print(coding)
# if coding:
#     nwords = []
#     for word in words:
#         if len(word) >= 3:
#             r1 = "".join(ran.choices(letters, k=3))
#             r2 = "".join(ran.choices(letters, k=3))
#             stnew = r1 + word[1:] + word[0] + r2
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))

# else:
#     nwords = []
#     for word in words:
#         if len(word) >= 3:
#             stnew = word[3:-3]
#             stnew = stnew[-1] + stnew[:-1]
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))

# # print(nwords)


# unconfirmed = ['alice', 'brian', 'candace']
# confirmed_users = []

# while unconfirmed:
#     current = unconfirmed.pop()
    
#     print("verifying user: "+ current.title())
#     confirmed_users.append(current)
    
# print("the confirmed users are :")
# for i in confirmed_users:
#     print(i)

response =  { }
polling  = True
while polling :
    name = input("what is your name : ")
    respo = input("which mountain do you want climb : " )
    response[name] = respo
    
    
    repeat = input("do you want to dd another person yes/no : ")
    if repeat  == "no":
        polling = False
        
print("\n......poll result ........")
for name, respo in response.items():
    print(name +"would like to climb"+ respo)