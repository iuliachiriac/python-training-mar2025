x = 0  # global variable


def func(a):
    b = "b"  # local variable
    print("inside func:", a, b, x)


func(25)
func(42)
print("outside func:", x)
