def func1():
    """Print greetings"""
    print("Buna dimineata")


# type hints
def prod(x: str, y: int = None):
    print(x * y)


# print(__name__)
if __name__ == "__main__":
    help(func1)
    prod("hello", 3)
    prod(5.3, 3)
