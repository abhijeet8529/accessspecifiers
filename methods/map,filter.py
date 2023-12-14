# # MAP............................................................................x

from functools import reduce


def cube(x):
    return x*x*x


# # print(cube(2))


lis = [1, 2, 3, 4, 5, 6]
newl = []
# for item in lis:
#     newl.append(cube(item))
# print(newl)
newl = list(map(lambda x: x*x*x, lis))
print(newl)

# # filter.........................................................................x


def filterfunc(a):
    return a > 4


newnewl = (list(filter(filterfunc, lis)))
print(newnewl)


# REDUCE.............................................................................x


new = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, new)
print(sum)
