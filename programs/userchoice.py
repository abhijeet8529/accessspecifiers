print(
    " 1: For area of circle\n",
    "2: For area of rectangle \n",
    "3: For circumference of circle\n",
    "4: For area of square \n",
)
while True:
    choice = int(input("Enter according to your choice or 0 to exit : "))
    if choice == 1:
        r = int(input("enter the radius of the circle : "))
        area = 3.14 * r * r
        print("the radius of the circle is :", area)
    elif choice == 2:
        l = int(input("Enter the length :"))
        b = int(input("Enter the breadth :"))
        area = l * b
        print("the area of the rectangle is :", area)
    elif choice == 3:
        r = int(input("Enter the radius of the circle : "))
        c = 2 * (int(3.14 * r))
        print("the radius of the circle is :", c)
    elif choice == 4:
        l = int(input("enter the length of sqaure : "))
        area = l * l
        print("the area of the square is :", area)
    else:
        print(choice, "is invalid vedya")
        break
