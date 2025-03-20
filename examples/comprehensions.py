# Dict comprehension
d1 = {i: i**2 for i in range(1, 10) if i % 2 == 1}
d2 = {i: f'City{i}' for i in range(1, 5)}

# Set comprehension
s1 = {f'City{i}' for i in range(1, 5)}
s2 = {i**2 for i in range(10) if i % 2 == 1}
