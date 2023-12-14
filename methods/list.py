lst = [i for i in range(10)]
print(lst)
lst = [i * i for i in range(10) if i % 2 == 0]
print(lst)
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [i for i in names if "o" in i]

print(namesWith_O)
