l = [1, 11, 45, 2, 1, 1, 1, 5, 7]
print(l)
l.append(8)
l.sort(reverse=True)
l.reverse()
print(l.index(2))
print(l.count(1))
m = l.copy()
l.insert(1, 899)
m[0] = 0
m = [900, 1000, 100]
k = l + m
# l.extend(m)
print(k)
print(l)
