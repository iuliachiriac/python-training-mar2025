my_path = r"D:\Ceva\Altceva\nanana"  # for Windows paths, use raw strings

with open("imports.py", "r") as f:
    print("inside `with` block, file is closed:", f.closed)
    for line in f:
        if line.startswith("#"):
            print(line.strip())

print("after `with` block, file is closed:", f.closed)

