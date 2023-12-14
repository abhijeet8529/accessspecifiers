def factorial(num):
    if (num == 1 and num == 0):
        return 1
    else:
        return (num * factorial(num - 1))


num = 7
print("number:", num)
print("factorial is : ", factorial(num))


def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))


# Driver Code
num = 7
print("Number: ", num)
print("Factorial: ", factorial(num))


class school:
    def __init__(self, name, sub):
        self.name = name
        self.sub = sub


class marks(school):
    def __init__(self, name, sub, mark):
        super().__init__(name, sub)
        self.mark = mark

    def info(self):
        print(f"the student {self.name} from subject {
              self.sub} got {self.mark} marks")


a = marks("abhijeet", "commerce", "100/200")
a.info()
