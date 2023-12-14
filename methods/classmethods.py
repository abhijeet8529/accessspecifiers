# class emp:
#     company = "apple"

#     def show(self):
#         print(f"the employess works in the company {self.company}")

#     @classmethod
#     def empclass(cls, companyname):
#         cls.company = companyname


# emp1 = emp()
# emp1.show()
# emp1.empclass("tesla")
# emp1.show()
# print(emp.company)e1employee:
class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def frmstr(cls, string):
        return cls(string.split(",")[0], string.split(",")[1])


e1 = employee("abhijeet", 12000)
print(e1.name)
print(e1.age)
string = "rohan, 32321"
e2 = employee.frmstr(string)
print(e2.name)
print(e2.age)
