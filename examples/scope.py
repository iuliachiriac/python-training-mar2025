x = 0  # global variable


def func(a):
    b = "b"  # local variable
    # shadowing of global variable (it is recommended to avoid shadowing names)
    # x = 100
    print("inside func:", a, b, x)


# sum = 0  # shadowing of a built-in name
func(25)
func(42)
print("outside func:", x)
