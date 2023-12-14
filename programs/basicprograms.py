cels = float(input("enter the celsius :"))
print("the celcius is ", cels)
f = cels * 9 / 5 + 32
print("the fahrenhiet is ", f)
name = "neeru"
age = 21
print(name, " you are age ", age)
print(
    "and next year u will be",
    age + 1,
)
cp = int(input(" enter cp "))
profit = int(input("enter the profit : "))
sp = cp + profit
# print("the selling price is : ", sp)
a = input("enter school")
b = input("enter class")
c = input("enter section ")
# print(a, "-",b,"-",c)
dollar = int(input("enter the dollar amount: "))
rupee = 83.28 * dollar
print("the amount in rupee : rs", rupee)
x = 4
y = x + 1
x = 20, y + x
print(x, y)
a = int(input("enter the number"))
b = int(input("enter the number"))
c = int(input("enter the number"))
big = a
if b >= big:
    print("the big number is b :", b)
elif c >= big:
    print("the big number is c ", c)
else:
    print(" a is the biggest", a)
var = 1
while var == 1:
    num = int(input("enter a number : "))
    print(" you entered :", num)

print(" bye")
i = 2
while i >= 0:
    j = 2
    while j >= 0:
        print(2, end="")
        j = j - 1
    print()
    i = i - 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
