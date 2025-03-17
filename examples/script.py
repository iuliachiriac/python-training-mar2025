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
