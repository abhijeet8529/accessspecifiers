def greet(fx):
    def mfx(*args, **kwargs):
        print("good morning boss!")
        fx(*args, **kwargs)
        print("have a nice day with this function")
    return mfx


@greet
def hello():
    print("hello world")


@greet
def add(a, b):
    print(a + b)


hello()
add(5, 5)
