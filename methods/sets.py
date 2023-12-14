# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities) //union method
# cities.update(cities2) // update
# print(cities,cities2)
# cities3 = cities.intersection(cities2) // intersection
# print(cities3)
# cities.intersection_update(cities2) //intersection update
# cities3 = cities.symmetric_difference(cities2) // symmetric difference
# print(cities3)
# cities.add("helsinki ") #Adding
# cities.remove("Berlin")
# s1 = {"abhijeet" , 12 , 5.6 , True}
# if "abhijeet" in s1 :
#     print("yes, its there!")
# else:
#     print("no its not")
def update(a, *args):
    c = a
    for i in args:
        c = c + 1
    print(c)

update(5,12,12,40)