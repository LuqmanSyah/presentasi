# File Handling Modes in Python

# Mode 'r' (Read-Only)
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print("Mode 'r' (Read-Only):")
        print(content)
except FileNotFoundError:
    print("File not found for mode 'r'.")

# Mode 'w' (Write)
with open("example.txt", "w") as file:
    file.write("This is a new file.\n")
    file.write("All previous content is overwritten.")
print("\nMode 'w' (Write): File overwritten.")

# Mode 'a' (Append)
with open("example.txt", "a") as file:
    file.write("\nThis line is appended to the file.")
print("\nMode 'a' (Append): Content appended.")

# Mode 'x' (Exclusive Creation)
try:
    with open("new_file.txt", "x") as file:
        file.write("This file is newly created.")
    print("\nMode 'x' (Exclusive Creation): File created.")
except FileExistsError:
    print("\nMode 'x' (Exclusive Creation): File already exists!")