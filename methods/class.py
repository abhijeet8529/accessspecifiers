# class person:
#     def __init__(self, n, o):
#         self.name = n
#         self.occ = o

#     def info(self):
#         print(f"{self.name} is a {self.occ} by profession ")


# a = person("abhijeet", "artist")
# a.info()


class employee:
    def parent(self):
        print("this is parent class")

class child(employee):
    def parent(self):
        print("abhijeet")
        super().parent()
    def childclass(self):
        print("this is child class")
        super().parent()

a = child()
a.childclass()
# a.parent()
