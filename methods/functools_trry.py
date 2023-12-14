from functools import lru_cache
import time
@lru_cache(maxsize = None)
def fx(n):
    time.sleep(4)
    return n*5
print(fx(2))
print(fx(4))
print(fx(5))
print(fx(7))
#.....................
print(fx(2))
print(fx(4))
print(fx(5))
print(fx(7))