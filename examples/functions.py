def func1():
    """Print greetings"""
    print("Buna dimineata")


# type hints
def prod(x: str, y: int):
    print(x * y)


help(func1)
prod("hello", 3)
prod(5.3, 3)
