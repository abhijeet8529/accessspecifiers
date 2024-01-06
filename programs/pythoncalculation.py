# a = int(input("enter the number : "))
# b = int(input("enter the number : : "))
# o = input("enter the operator : ")
# if o == "+":
#     print(a + b)
# elif o == "-":
#     print(a - b)
# elif o == "*":
#     print(a * b)
# elif o == "/":
#     print(a / b)
# elif o == "%":
#     print(a % b)
# elif o == "**":
#     print(a**b)
# else:
#     print("invalid operator")
import tkinter as tk

def evaluate(event=None):
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a string variable to store the result
result = tk.StringVar()

# Create an entry widget for input
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
entry.bind("<Return>", evaluate)

# Create a label to display the result
label = tk.Label(root, textvariable=result, width=30)
label.pack(pady=10)

# Create buttons for numbers and operations
buttons = [
    ("7", 1, 1), ("8", 1, 2), ("9", 1, 3),
    ("4", 2, 1), ("5", 2, 2), ("6", 2, 3),
    ("1", 3, 1), ("2", 3, 2), ("3", 3, 3),
    ("0", 4, 2), ("+", 1, 4), ("-", 2, 4),
    ("*", 3, 4), ("/", 4, 4), ("=", 4, 3)
]

for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, command=lambda t=text: entry.insert(tk.END, t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Create a clear button
clear_btn = tk.Button(root, text="Clear", command=lambda: entry.delete(0, tk.END))
clear_btn.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()
