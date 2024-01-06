# # def multiadd(a, b):
# #     product = a * b
# #     if product <= 1000:
# #         return product
# #     else:
# #         return a + b


# # result = multiadd(20, 40)
# # print("the product prize is : ", result)
# # result = multiadd(40, 90)
# # print("the product prize is : ", result)
# # print("the previuos and current number :")
# # previousnum = 0
# # for i in range(1, 11):
# #     sumx = previousnum + i
# #     print("current number :", i, " previous number", previousnum, "sum : ", sumx)
# #     previousnum = i

# # a = input("enter your string: ")
# # print("original string : ", a)
# # size = len(a)
# # for i in range(0, size - 1, 2):
# #     print("index[", i, "]", a[i])

# # a = input("enter your string: ")
# # print("original string : ", a)
# # x = list(a)
# # for i in x[0::2]:
# #     print(i)


# theword = input("enter word : ")


# def new1(a, b):
#     try:
#         if theword == str():
#             print("the new word is :", theword.replace(a, b))
#             return theword
#     except:
#         print("the entered value is not string")


# new1('p', 'l')


# # theword = input("enter word : ")

# # def new1(a,b):

# #     for character in theword:
# #             print(theword.replace(a,b))
# #             break
# # new1('a','f')


# # name = input("enter your name :")
# # # print(f"you deserve aand bhaat {name}")
# # theword = input("enter word : ")
# # integer = int(theword)
# # if integer != (""):
# #     print("u need bada wala aand")

# # else:
# #     # print("u eat aand bhaat")

# # # ? dictionary:
# #  info={"name": "abhijeet", "country": "india", "salary": 80, "eligible": True}
# # print(info)
# # print(info["name"])
# # print(info.get("eligible")) #*only access one value .get
# # print(info.keys())  # *access only keys
# # print(info.values())  # *access only values
# # print(info.items())  # *access only items in pair
# # for key, values in info.items():
# #     print(
# #         f"the value corresponding to the {key} is {values}"
# #     )  # *access correspomdimg of key

# # for key in info.keys():
# #     print(
# #         f"the value corresponding to the {key} is {info[key]}"
# #     )  # *access correspomdimg of key

# # #! dictionary methods
# # ep1 = {1: 234, 2: 432, 3: 489, 4: 675, 5: 111}
# # ep2 = {7: 333, 9: 444}
# # ep1.update(ep2)  # ? for key
# # ep1.clear()  # ? for clear
# # ep1.pop(1)  # ? for pop value
# # del ep1[1]  # ? for del dictionary or anyy value/key
# # print(ep1)


# # i = 0
# # while i < 7:
# #     print(i)
# #     i = i + 1
# #     if i == 4:
# #         break
# # else:
# #     print("no i sorry")
# # x = 5
# # while x < 10:
# #     print(x + 10)
# #     x += 2
# # for x in range(5, 10, 2):
# #     print(x + 10)

# # for k in range(10, 20, 5):
# #     print(k)

# # x = 10
# # y = 0
# # while x > y:
# #     x = x - 4
# #     y += 4
# # #     print(x, end="")
# # a = int(input("enter the first number : "))

# # b = int(input("enter the second number : "))

# # c = int(input("enter the third number : "))
# # if a > b:
# #     if a > c:
# #         print("a is the graeatest number ")
# #     else:
# #         print("c is the graeatest number ")
# # else:
# #     if b > c:
# #         print("b is the graeatest number ")
# #     else:
# #         print("c is the graeatest number ")

# # s = 0
# # n = int(input("enter the limit: "))
# # for i in range(n + 1):
# #     if i % 2 == 0:
# #         s += 1
# # print(s)
# a = input("enter the names : ")
# b = []
# b = a.split(",")
# print(b)
# c = 0
# lst2 = []
# for i in b:
#     if len(i) < 6:
#         lst2.append(i)
#         c = c + 1
# print("user name below 5 are :" , c)
# print(lst2)

# import pandas
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Toggle Background</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            transition: background-color 0.3s ease;
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
    </style>
</head>

<body id="body">

    <button onclick="toggleBackground()">Toggle Background</button>

    <script>
        function toggleBackground() {
            var body = document.getElementById("body");
            if (body.style.backgroundColor === "white" || body.style.backgroundColor === "") {
                body.style.backgroundColor = "lightgray";
            } else {
                body.style.backgroundColor = "white";
            }
        }
    </script>

</body>

</html>
