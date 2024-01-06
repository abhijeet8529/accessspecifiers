x = [1, 2, 3]
print(dir(x))
print(x.__add__)  # ? dir method(shows all avilable methods)


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.profession = "artist"


p = person("abhijeet", 21)
# print(p.name)
# print(p.age)
p.profession = "hero"
print(p.profession())
print(p.__dict__)  # ? __dict__ useful for understanding values
# print(help(person))  # ? help for understanding the selected code
