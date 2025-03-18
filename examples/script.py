# name = "world"
name = "Iulia"  # initializing name variable
print("hello " + name + "!")

multiline_str = """
mere
pere
banane
"""
print(multiline_str)

distance = 5.7212
print("Iulia walked 5.12km.")
print(name, "walked", round(distance, 2), "km.")
message = name + " walked " + str(round(distance, 2)) + "km."
print(message)

message = f"{name} walked {distance:.2f}km."
print(message)

greeting = input("Hello!\n")
print(greeting)
print(len(greeting))

long_line = "For multiples of three print Fizz instead of the number and for "\
            "the multiples of five print Buzz instead of the n"

long_line = ("For multiples of three print Fizz instead of the number and for "
             "the multiples of five print Buzz instead of the n")

if (greeting and len(greeting) > 10 and ("m" in greeting or "s" in greeting)
        and "!" in greeting):
    print("ok")
