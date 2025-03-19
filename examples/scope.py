x = 0  # global variable


def func(a):
    b = "b"  # local variable
    # shadowing of global variable (it is recommended to avoid shadowing names)
    # x = 100
    print("inside func:", a, b, x)


def remove_all(values, val):
    print("inside func", id(values), values is my_list)
    while val in values:
        values.remove(val)
    return values


def remove_vowels(text):
    print("inside func", id(text), text is my_text)
    for vowel in "aeiouAEIOU":
        if vowel in text:
            text = text.replace(vowel, "")
            print("inside func", id(text), text is my_text)
    return text


# sum = 0  # shadowing of a built-in name
func(25)
func(42)
print("outside func:", x)

my_list = [2, 3, 5, 71, 3, 4, 3]
print("in global, id(my_list)", id(my_list))
ret_list = remove_all(my_list, 3)
print(ret_list)
print(my_list)

my_text = "good evening world"
print("in global, id(my_text)", id(my_text))
ret_text = remove_vowels(my_text)
print(my_text)
print(ret_text)
