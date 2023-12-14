a = int(input("enter the number : "))
b = int(input("enter the number : : "))
o = input("enter the operator : ")
if o == "+":
    print(a + b)
elif o == "-":
    print(a - b)
elif o == "*":
    print(a * b)
elif o == "/":
    print(a / b)
elif o == "%":
    print(a % b)
elif o == "**":
    print(a**b)
else:
    print("invalid operator")
